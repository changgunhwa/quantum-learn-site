
document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("simForm");
  const output = document.getElementById("result");
  const canvasContainer = document.getElementById("canvasContainer");

  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(75, 1, 0.1, 1000);
  const renderer = new THREE.WebGLRenderer({ antialias: true });
  renderer.setSize(300, 300);
  canvasContainer.appendChild(renderer.domElement);

  camera.position.z = 3;

  const sphereGeometry = new THREE.SphereGeometry(1, 32, 32);
  const wireframe = new THREE.WireframeGeometry(sphereGeometry);
  const line = new THREE.LineSegments(wireframe, new THREE.LineBasicMaterial({ color: 0x4444ff }));
  scene.add(line);

  const arrowDir = new THREE.Vector3(0, 1, 0);
  const arrowHelper = new THREE.ArrowHelper(arrowDir, new THREE.Vector3(0, 0, 0), 1, 0x00ffff);
  scene.add(arrowHelper);

  renderer.render(scene, camera);

  form.addEventListener("submit", (e) => {
    e.preventDefault();

    const a = parseFloat(document.getElementById("real").value);
    const b = parseFloat(document.getElementById("imag").value);

    if (isNaN(a) || isNaN(b)) {
      output.textContent = "Please enter valid real and imaginary parts.";
      return;
    }

    const norm = Math.sqrt(a ** 2 + b ** 2);
    const theta = 2 * Math.acos(a / norm);
    const phi = Math.atan2(b, a);

    const x = Math.sin(theta) * Math.cos(phi);
    const y = Math.sin(theta) * Math.sin(phi);
    const z = Math.cos(theta);

    arrowHelper.setDirection(new THREE.Vector3(x, y, z).normalize());
    renderer.render(scene, camera);

    output.innerHTML = `
      <strong>Normalized:</strong> ${norm.toFixed(3)}<br>
      <strong>Theta (θ):</strong> ${theta.toFixed(3)} rad<br>
      <strong>Phi (φ):</strong> ${phi.toFixed(3)} rad
    `;
  });
});
