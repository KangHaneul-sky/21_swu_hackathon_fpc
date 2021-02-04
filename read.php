<?php
  $db_host = "localhost";
  $db_user = "hackathon";
  $db_passwd = "dothome1!";
  $db_name = "hackathon";
  $conn = mysqli_connect($db_host,$db_user,$db_passwd,$db_name);

  if (mysqli_connect_errno($conn)) {
    echo mysqli_connect_error();
    exit();
  }

  $mode = $_GET["mode"];
  if($mode == 1){
    $query = "SELECT * FROM data Where finger='".$_GET["finger"]."'";
    $result = mysqli_query($conn,$query);
    while($row = mysqli_fetch_array($result)){ // mysqli_fetch_array 함수를 사용하여 값을 가져옴
      echo "{age:".$row["age"].",birthday:".$row["birthday"].",finger:".$row["finger"].",address:".$row["address"]."}";
    }
  }
  else if($mode == 2){
    echo "mode = 2";
  }

  // echo 'Hello ' . htmlspecialchars($_GET["name"]) . '!';

  mysqli_close($conn);
?>