<?php
$path = "uploads/";
$files = scandir($path);
foreach ($files as &$value) {
    echo "<a href='http://localhost/".$value."' target='_blank' >".$value."</a><br/><br/>";
}
?>