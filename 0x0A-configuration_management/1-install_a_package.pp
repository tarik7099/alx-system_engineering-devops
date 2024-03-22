# Puppet manifest to install Flask using pip3

package { 'flask':
  ensure   => '2.1.0',  # Specify the version of Flask to install
  provider => 'pip3',   # Use pip3 as the provider
  require  => Package['python3-pip'], # Ensure pip3 is installed first
}

