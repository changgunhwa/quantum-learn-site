from flask import Flask, request, render_template, send_file
import numpy as np
import matplotlib.pyplot as plt
from qutip import *
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/simulate', methods=['POST'])
def simulate():
    # 입력 파라미터 받기
    Omega_input = float(request.form.get('Omega', 0.1))  # 기본값 0.1

    # 시뮬레이션 파라미터 설정
    omega_0 = 2 * np.pi * 1.0   # 2.8GHz 정규화
    Omega = 2 * np.pi * Omega_input
    tlist = np.linspace(0, 10, 1000)
    psi0 = basis(2, 0)

    def phi_target(t, args): return 0.1 * np.sin(0.5 * t)
    def phi_no_target(t, args): return 0

    def H_with_phase(phi_func):
        return [omega_0 * sigmaz(),
                [sigmax(), lambda t, args: Omega * np.cos(omega_0 * t + phi_func(t, args))]]

    result_target = mesolve(H_with_phase(phi_target), psi0, tlist, [], [sigmaz()])
    result_no_target = mesolve(H_with_phase(phi_no_target), psi0, tlist, [], [sigmaz()])

    # 그래프 생성
    plt.figure()
    plt.plot(tlist, result_target.expect[0], label='With Target')
    plt.plot(tlist, result_no_target.expect[0], label='No Target', linestyle='--')
    plt.xlabel("Time")
    plt.ylabel("⟨σ_z⟩ (Spin Projection)")
    plt.title(f"NIO 양자 스텔스 탐지 (Omega = {Omega_input})")
    plt.legend()
    plt.grid(True)

    # 이미지 버퍼에 저장
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()

    return send_file(img, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
