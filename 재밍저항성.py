from qutip import *
import numpy as np
import matplotlib.pyplot as plt

# 파라미터 (2.8GHz → 너무 크므로 정상화된 값으로 임시 시뮬레이션)
omega_0 = 2 * np.pi * 1.0  # 1.0 (정규화, GHz → 1 단위)
Omega = 2 * np.pi * 0.05   # 상대적 Rabi 주파수

tlist = np.linspace(0, 10, 1000)  # 단위 시간에서 시뮬레이션 (0 ~ 10)

psi0 = basis(2, 0)

# 시간 의존 해밀토니안 정의
H0 = omega_0 * sigmaz()
H1 = [sigmax(), lambda t, args: Omega * np.cos(omega_0 * t + np.random.normal(0, 0.05))]

H = [H0, H1]

# 적분기 옵션 강화
opts = Options(nsteps=10000, max_step=0.1)

# 시뮬레이션 수행
result = mesolve(H, psi0, tlist, [], [sigmax(), sigmay(), sigmaz()], options=opts)

# 결과 출력
plt.plot(tlist, result.expect[2], label='⟨σ_z⟩')
plt.xlabel('Time (arb. unit)')
plt.ylabel('Spin Projection')
plt.title('항재밍 시뮬레이션 (정규화된 2.8GHz 시스템)')
plt.legend()
plt.grid(True)
plt.show()
