$recaptcha = $_POST['g-recaptcha-response'];
$res = reCaptcha($recaptcha);
if($res['success']){
    // Send email
}else{
    // Error
}

function reCaptcha($recaptcha){
    $secret = "6Levo08eAAAAAMlg-IVaV6_a1VN5OuVz8VlrW85I";
    $ip = $_SERVER['REMOTE_ADDR'];
    // $postvars = array("6Levo08eAAAAAMlg-IVaV6_a1VN5OuVz8VlrW85I"=>$secret, "response"=>$recaptcha, "remoteip"=>$ip);  
    $url = "https://www.google.com/recaptcha/api/siteverify";
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_TIMEOUT, 10);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $postvars);
    $data = curl_exec($ch);
    curl_close($ch);
    return json_decode($data, true);
}

function hid() {
    var x = document.getElementById("password");
    if (x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
}

function imagefun() {
    var Image_Id = document.getElementById('getImage');
    if (Image_Id.src.match("../static/images/eye.png")) {
        Image_Id.src = "../static/images/c-eye.png";
    }
    else {
        Image_Id.src = "../static/images/eye.png";
    }
}

function hide() {
    var x = document.getElementById("pass");
    if (x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
}

function imagefu() {
    var Image_Id = document.getElementById('getImag');
    if (Image_Id.src.match("../static/images/eye.png")) {
        Image_Id.src = "../static/images/c-eye.png";
    }
    else {
        Image_Id.src = "../static/images/eye.png";
    }
}

function matchPassword() {
    var pw1 = document.getElementById("password");
    var pw2 = document.getElementById("con-pass");
    if(pw1 != pw2)  
    {
      alert("Passwords did not match");
    } else {
      alert("Password created successfully");
    } 
  }