
!pip install qutip


from qutip import *
import numpy as np
import matplotlib.pyplot as plt

# 시뮬레이션 파라미터
omega_0 = 2 * np.pi * 1.0   # 정규화된 2.8GHz
Omega = 2 * np.pi * 0.1
tlist = np.linspace(0, 10, 1000)
psi0 = basis(2, 0)

# 위상 함수 (표적 존재 여부에 따른 변화)
def phi_target(t, args): return 0.1 * np.sin(0.5 * t)  # 표적 반사 위상 변화
def phi_no_target(t, args): return 0  # 표적 없을 경우

# 시간의존 해밀토니안
def H_with_phase(phi_func):
    return [omega_0 * sigmaz(),
            [sigmax(), lambda t, args: Omega * np.cos(omega_0 * t + phi_func(t, args))]]

# 시뮬레이션 실행
result_target = mesolve(H_with_phase(phi_target), psi0, tlist, [], [sigmaz()])
result_no_target = mesolve(H_with_phase(phi_no_target), psi0, tlist, [], [sigmaz()])

# 결과 비교 시각화
plt.plot(tlist, result_target.expect[0], label='With Target')
plt.plot(tlist, result_no_target.expect[0], label='No Target', linestyle='--')
plt.xlabel("Time")
plt.ylabel("⟨σ_z⟩ (Spin Projection)")
plt.title("NIO 이온양자 스텔스 표적 탐지 (2.8GHz)")
plt.legend()
plt.grid(True)
plt.show()
