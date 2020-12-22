<?php
 $host="localhost";
 $user="username";
 $pass="password";
 $db="db_work";
 $dbh= new PDO("mysql:host=$host;dbname=$db",$user,$pass);
 $dbh->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

$result = $dbh->prepare("SELECT * FROM db_work");
$result->execute();
$return = [];
 foreach ($result as $row) {
    $return[] = [
       'firstName' => $row['firstName'],
       'lastName' => $row['lastName']
    ];
 }
 $dbh = null;

 header('Content-type: application/json');
 echo json_encode($return);

?>