#!/usr/bin/pup
#Install the puppe
# t-lint package
package { 'flask':
  ensure   => '2.5.0',
  provider => 'pip3',
}
