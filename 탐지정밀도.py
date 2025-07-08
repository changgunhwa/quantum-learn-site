import numpy as np
import matplotlib.pyplot as plt
from qutip import *

# 기본 파라미터
GHz = 1e9
f = 2.8 * GHz                  # 주파수 2.8GHz
w = 2 * np.pi * f              # 각진동수
T = 5e-9                       # 파형 지속시간 (5ns)
phi_target = np.pi / 8         # 물체 존재 시 위상 지연
phi_no_target = 0              # 물체 없음

# 상태 정의 (기저 상태: |0> = |↑⟩, |1> = |↓⟩)
psi0 = (basis(2, 0) + basis(2, 1)).unit()  # 초기 상태: 균일 중첩 상태

# 해밀토니안: 물체 유무에 따른 위상 변화
def H_with_phase(phase_shift):
    H = 0.5 * w * (sigmax() * np.cos(phase_shift) + sigmay() * np.sin(phase_shift))
    return H

# 시간 리스트
times = np.linspace(0, T, 200)

# 시뮬레이션: 물체 없음 vs 있음
result_no_target = mesolve(H_with_phase(phi_no_target), psi0, times, [], [sigmax(), sigmay(), sigmaz()])
result_target = mesolve(H_with_phase(phi_target), psi0, times, [], [sigmax(), sigmay(), sigmaz()])

# 결과 시각화
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.title("📡 Without Object (No Phase Shift)")
plt.plot(times * 1e9, result_no_target.expect[0], label='⟨σx⟩')
plt.plot(times * 1e9, result_no_target.expect[1], label='⟨σy⟩')
plt.plot(times * 1e9, result_no_target.expect[2], label='⟨σz⟩')
plt.xlabel("Time (ns)")
plt.ylabel("Expectation values")
plt.legend()

plt.subplot(1, 2, 2)
plt.title("📡 With Object (Phase Shift π/8)")
plt.plot(times * 1e9, result_target.expect[0], label='⟨σx⟩')
plt.plot(times * 1e9, result_target.expect[1], label='⟨σy⟩')
plt.plot(times * 1e9, result_target.expect[2], label='⟨σz⟩')
plt.xlabel("Time (ns)")
plt.ylabel("Expectation values")
plt.legend()

plt.tight_layout()
plt.show()
