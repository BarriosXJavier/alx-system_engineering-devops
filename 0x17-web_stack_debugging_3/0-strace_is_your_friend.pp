# Fix "phpp" extension error to php in "wp-settings.php"

exec{'fix-wordpress':
	command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
	path    => ['/bin', '/usr/bin/', '/usr/local/bin/'],
}