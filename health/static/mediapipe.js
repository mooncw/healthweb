const video5 = document.getElementsByClassName('input_video5')[0];
const out5 = document.getElementsByClassName('output5')[0];
const controlsElement5 = document.getElementsByClassName('control5')[0];
const canvasCtx5 = out5.getContext('2d');

const fpsControl = new FPS();

const spinner = document.querySelector('.loading');
spinner.ontransitionend = () => {
  spinner.style.display = 'none';
};

const name_en = document.getElementById('name_en');
name_en.style.display = 'none'; // H1 태그를 숨김
const kind = name_en.innerText; // H1 태그의 텍스트를 변수에 할당
// alert(kind); // 변수 값 출력


var count = 0;
var cur_status = 'none';

function reset_click() {
  count = 0;
}

function zColor(data) {
  const z = clamp(data.from.z + 0.5, 0, 1);
  return `rgba(0, ${255 * z}, ${255 * (1 - z)}, 1)`;
}

function onResultsPose(results) {
  document.body.classList.add('loaded');
  fpsControl.tick();

  canvasCtx5.save();
  canvasCtx5.clearRect(0, 0, out5.width, out5.height);
  canvasCtx5.drawImage(
    results.image, 0, 0, out5.width, out5.height);
  drawConnectors(
    canvasCtx5, results.poseLandmarks, POSE_CONNECTIONS, {
    color: (data) => {
      const x0 = out5.width * data.from.x;
      const y0 = out5.height * data.from.y;
      const x1 = out5.width * data.to.x;
      const y1 = out5.height * data.to.y;

      const z0 = clamp(data.from.z + 0.5, 0, 1);
      const z1 = clamp(data.to.z + 0.5, 0, 1);

      const gradient = canvasCtx5.createLinearGradient(x0, y0, x1, y1);
      gradient.addColorStop(
        0, `rgba(0, ${255 * z0}, ${255 * (1 - z0)}, 1)`);
      gradient.addColorStop(
        1.0, `rgba(0, ${255 * z1}, ${255 * (1 - z1)}, 1)`);
      return gradient;
    }
  });
  drawLandmarks(
    canvasCtx5,
    Object.values(POSE_LANDMARKS_LEFT)
      .map(index => results.poseLandmarks[index]),
    { color: zColor, fillColor: '#FF0000' });
  drawLandmarks(
    canvasCtx5,
    Object.values(POSE_LANDMARKS_RIGHT)
      .map(index => results.poseLandmarks[index]),
    { color: zColor, fillColor: '#00FF00' });
  drawLandmarks(
    canvasCtx5,
    Object.values(POSE_LANDMARKS_NEUTRAL)
      .map(index => results.poseLandmarks[index]),
    { color: zColor, fillColor: '#AAAAAA' });


  // degree
  function get_dot(v1, v2) {
    let result = 0;
    for (let i = 0; i < 3; i++) {
      result += v1[i] * v2[i];
    }
    return result;
  }

  function get_norm(v1) {
    let result = 0;
    for (let i = 0; i < 3; i++) {
      result += v1[i] * v1[i];
    }
    return Math.sqrt(result)
  }

  function get_pro_degree(A, B) {
    let v1 = [A.x - B.x, A.y - B.y, A.z - B.z];
    let v2 = [A.x - B.x, 0, A.z - B.z];
    let cosin = get_dot(v1, v2) / (get_norm(v1) * get_norm(v2));
    let degree = Math.acos(cosin) * 180 / Math.PI;
    return degree
  }

  function get_degree(A, B, C) {
    let v1 = [A.x - B.x, A.y - B.y, A.z - B.z];
    let v2 = [C.x - B.x, C.y - B.y, C.z - B.z];
    let cosin = get_dot(v1, v2) / (get_norm(v1) * get_norm(v2));
    let degree = Math.acos(cosin) * 180 / Math.PI;
    return degree
  }


  // push up
  function get_direction(results) {
    let left = results.poseLandmarks[12].z;
    let right = results.poseLandmarks[11].z;
    if (left > right) {
      return 'right'
    } else if (right >= left) {
      return 'left'
    } else {
      return 'none'
    }
  }

  function get_push_ready(results, dir) {
    let ready = 'notready'
    if (dir == 'right') {
      let right_hip = results.poseLandmarks[23]   //24
      let right_ankle = results.poseLandmarks[27]   //28

      let right_ankle_visibility = results.poseLandmarks[27].visibility

      let degree = get_pro_degree(right_hip, right_ankle)

      if (degree <= 60 && right_ankle_visibility > 0.5) {
        ready = 'ready'
      }
      return ready
    }
    else if (dir == 'left') {
      let left_hip = results.poseLandmarks[24]
      let left_ankle = results.poseLandmarks[28]

      let left_ankle_visibility = results.poseLandmarks[28].visibility

      let degree = get_pro_degree(left_hip, left_ankle)

      if (degree <= 60 && left_ankle_visibility > 0.5) {
        ready = 'ready'
      }
      return ready
    }
    return ready
  }

  function get_pushup_status(results, dir) {
    let status = 'none'
    if (dir == 'right') {
      let right_wrist = results.poseLandmarks[15]  //16
      let right_elbow = results.poseLandmarks[13]  //14
      let right_shoulder = results.poseLandmarks[11]  //12

      let right_degree = get_degree(right_wrist, right_elbow, right_shoulder)

      if (right_degree > 130) {
        status = 'up'
      } else {
        status = 'down'
      }
      return status
    } else if (dir == 'left') {
      let left_wrist = results.poseLandmarks[16]
      let left_elbow = results.poseLandmarks[14]
      let left_shoulder = results.poseLandmarks[12]

      let left_degree = get_degree(left_wrist, left_elbow, left_shoulder)

      if (left_degree > 130) {
        status = 'up'
      } else {
        status = 'down'
      }
      return status
    }
    return status
  }

  if (kind == 'pushup') {
    if (get_push_ready(results, get_direction(results)) == 'ready') {
      let status = get_pushup_status(results, get_direction(results))
      if (cur_status != status) {
        if (status == 'up') {
          if (cur_status == 'down') {
            count += 1
          }
        }
        cur_status = status
      }
    }
    // else {
    //   count = 0
    // }
  }


  //squat
  function get_squat_ready(results, dir) {
    let ready = 'notready'
    if (dir == 'right') {
      let right_hip = results.poseLandmarks[23]   //24
      let right_ankle = results.poseLandmarks[27]   //28

      let right_ankle_visibility = results.poseLandmarks[27].visibility

      let degree = get_pro_degree(right_hip, right_ankle)

      if (degree > 60 && right_ankle_visibility > 0.5) {
        ready = 'ready'
      }
      return ready
    }
    else if (dir == 'left') {
      let left_hip = results.poseLandmarks[24]
      let left_ankle = results.poseLandmarks[28]

      let left_ankle_visibility = results.poseLandmarks[28].visibility

      let degree = get_pro_degree(left_hip, left_ankle)

      if (degree > 60 && left_ankle_visibility > 0.5) {
        ready = 'ready'
      }
      return ready
    }
    return ready
  }

  function get_squat_status(results, dir) {
    let status = 'none'
    if (dir == 'right') {
      let right_ankle = results.poseLandmarks[27]  //28
      let right_knee = results.poseLandmarks[25]  //26
      let right_hip = results.poseLandmarks[23]  //24

      let right_degree = get_degree(right_ankle, right_knee, right_hip)

      if (right_degree > 110) {
        status = 'up'
      } else {
        status = 'down'
      }
      return status
    } else if (dir == 'left') {
      let left_ankle = results.poseLandmarks[28]
      let left_knee = results.poseLandmarks[26]
      let left_hip = results.poseLandmarks[24]

      let left_degree = get_degree(left_ankle, left_knee, left_hip)

      if (left_degree > 110) {
        status = 'up'
      } else {
        status = 'down'
      }
      return status
    }
    return status
  }

  if (kind == 'squat') {
    if (get_squat_ready(results, get_direction(results)) == 'ready') {
      let status = get_squat_status(results, get_direction(results))
      if (cur_status != status) {
        if (status == 'up') {
          if (cur_status == 'down') {
            count += 1
          }
        }
        cur_status = status
      }
    }
    // else {
    //   count = 0
    // }
  }


  // let testvalue = JSON.stringify(results.poseLandmarks[32].z);
  // let testvector = [1,2,3]
  document.getElementById("counting").innerHTML = count;
  // document.getElementById("counting").innerHTML=[count, kind, get_squat_ready(results, get_direction(results))];
  // document.getElementById("counting").innerHTML=get_pushup_status(results, get_direction(results));

  canvasCtx5.restore();
}

const pose = new Pose({
  locateFile: (file) => {
    return `https://cdn.jsdelivr.net/npm/@mediapipe/pose@0.2/${file}`;
  }
});
pose.onResults(onResultsPose);

const camera = new Camera(video5, {
  onFrame: async () => {
    await pose.send({ image: video5 });
  },
  width: 480,
  height: 480
});
camera.start();

new ControlPanel(controlsElement5, {
  selfieMode: true,
  upperBodyOnly: false,
  smoothLandmarks: true,
  minDetectionConfidence: 0.5,
  minTrackingConfidence: 0.5
})
  .add([
    new StaticText({ title: 'MediaPipe Pose' }),
    fpsControl,
    new Toggle({ title: 'Selfie Mode', field: 'selfieMode' }),
    new Toggle({ title: 'Upper-body Only', field: 'upperBodyOnly' }),
    new Toggle({ title: 'Smooth Landmarks', field: 'smoothLandmarks' }),
    new Slider({
      title: 'Min Detection Confidence',
      field: 'minDetectionConfidence',
      range: [0, 1],
      step: 0.01
    }),
    new Slider({
      title: 'Min Tracking Confidence',
      field: 'minTrackingConfidence',
      range: [0, 1],
      step: 0.01
    }),
  ])
  .on(options => {
    video5.classList.toggle('selfie', options.selfieMode);
    pose.setOptions(options);
  });