
<?php
$Usuario = $_POST["Usuario"];
$Contraseña = $_POST["Contraseña"];
if ($Usuario=="cliente" and $Contraseña=="cliente") {

    // Redireccionar directamente a new_page.html
     header( 'Location: http://www.yoursite.com/new_page.html' ) ;


}
elseif ($Usuario=="admin" and $Contraseña=="admin") {
		echo "Sos admin";
		header("Location:http://www.cristalab.com");
		# code...
	}
else{
echo "datos erroneos";
header("Location:http://www.cristalab.com");
}
?>
