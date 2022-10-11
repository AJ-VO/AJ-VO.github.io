<?php

if(isset($_POST['submit']))
 $mailto = "alexwinnable@gmail.com";//my email
 //getting match data
 $gagnant = $_POST['winner'];
 $perdant = $_POST['loser'];
 $point = $_POST['score'];
 $answer = "Match enregistré";//confirmation

 //Email
 $message = "Winner : " . $gagnant . "\n"
 . "Loser : " . $perdant . "\n"
 . "Score : " . $point . "\n" . $_POST['message'];

 $result = mail($mailto, $message);

 if ($result){
    $success = "Worked";
 } else {
    $failed = "Sorry!"
 }
?>