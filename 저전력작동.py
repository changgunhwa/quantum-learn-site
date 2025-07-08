
import numpy as np
import matplotlib.pyplot as plt


# 🧾 파라미터 설정
frequencies = [2.8e9]  # 2.8 GHz
pulse_durations = np.logspace(-9, -6, 100)  # 1ns ~ 1us
powers = [1e-6, 10e-6, 100e-6, 1e-3]  # 1μW ~ 1mW

# 📊 결과 저장
energy_per_pulse = {}  # [J]
energy_per_second = {}  # [W]

for P in powers:
    label = f"{P*1e6:.0f} μW"
    energy_per_pulse[label] = P * pulse_durations  # E = P × t
    energy_per_second[label] = energy_per_pulse[label] / pulse_durations  # P = E / t → 이론상 동일, 확인용

# 📈 시각화: 펄스당 소비 에너지
plt.figure(figsize=(10, 5))
for label in energy_per_pulse:
    plt.plot(pulse_durations * 1e9, energy_per_pulse[label] * 1e12, label=label)

plt.title("📡 펄스당 에너지 소비량 (2.8GHz NIO 이온양자 레이더)")
plt.xlabel("펄스 길이 (ns)")
plt.ylabel("에너지 (pJ)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# 📈 시각화: 초당 소비 전력 (이론 확인용)
plt.figure(figsize=(10, 5))
for label in energy_per_second:
    plt.plot(pulse_durations * 1e9, energy_per_second[label] * 1e6, label=label)

plt.title("⚡ 초당 소비 전력 (이론 확인)")
plt.xlabel("펄스 길이 (ns)")
plt.ylabel("전력 (μW)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
