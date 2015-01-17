<?php
header('Location: http://localhost:8888/output.html');
$file = 'log.txt';
$current = file_get_contents($file);
$target_dir = "uploads/";
$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
$uploadOk = 1;
$imageFileType = pathinfo($target_file,PATHINFO_EXTENSION);
// Check if image file is a actual image or fake image
if(isset($_POST["submit"])) {
    $check = getimagesize($_FILES["fileToUpload"]["tmp_name"]);
    if($check !== false) {
        $current .= "File is an image - " . $check["mime"] . ".";
        file_put_contents($file, $contents);
        $uploadOk = 1;
    } else {
        $current .= "File is not an image.";
        file_put_contents($file, $contents);
        $uploadOk = 0;
    }
}
// Check if file already exists
if (file_exists($target_file)) {
    $current .= "Sorry, file already exists.";
    file_put_contents($file, $contents);
    $uploadOk = 0;
}
// Check file size
if ($_FILES["fileToUpload"]["size"] > 500000) {
    $current .= "Sorry, your file is too large.";
    file_put_contents($file, $contents);
    $uploadOk = 0;
}
// Allow certain file formats
if($imageFileType != "jpg" && $imageFileType != "png" && $imageFileType != "jpeg"
&& $imageFileType != "gif" ) {
    $current .= "Sorry, only JPG, JPEG, PNG & GIF files are allowed.";
    file_put_contents($file, $contents);
    $uploadOk = 0;
}
// Check if $uploadOk is set to 0 by an error
if ($uploadOk == 0) {
    $current .= "Sorry, your file was not uploaded.";
    file_put_contents($file, $contents);
// if everything is ok, try to upload file
} else {
    if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) {
        $current .= "The file ". basename( $_FILES["fileToUpload"]["name"]). " has been uploaded.";
    } else {
        $current .= "Sorry, there was an error uploading your file.";
        file_put_contents($file, $contents);
    }
}

exec("python test_script.py");
?>