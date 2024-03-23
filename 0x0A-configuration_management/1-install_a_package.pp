#!/usr/bin/pup
#Install the puppe
# Install Flask package
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

# Install Werkzeug package
package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}
