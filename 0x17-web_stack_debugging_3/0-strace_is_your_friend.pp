#Fix phpp typo
exec { 'fix-wordpress':
	command => 'sed -i s/phpp/g /var/www/html/wp-settings.php',
	path	=> ['/bin', '/usr/bin', '/usr/local/bin'],
}
