---
subparsers:
    openstack:
        help: Provision systems using Ansible OpenStack modules
        groups:
            - title: image
              options:
                  image-name:
                      type: str
                      help: An image on OpenStack cloud to provision the instance with
                      required: yes
            - title: topology
              options:
                  network:
                      type: str
                      help: Network
                      default: default.yml
                  topology:
                      type: str
                      help: Provision topology.
                      default: "1_controller"
            - title: common
              options:
                  dry-run:
                      action: store_true
                      help: Only generate settings, skip the playbook execution stage
                  cleanup:
                      action: store_true
                      help: Clean given system instead of provisioning a new one
                  input:
                      action: append
                      type: str
                      short: i
                      help: Input settings file to be loaded before the merging of user args
                  output:
                      type: str
                      short: o
                      help: 'File to dump the generated settings into (default: stdout)'
                  extra-vars:
                      action: append
                      short: e
                      help: Extra variables to be merged last
                      type: str
                  from-file:
                      type: IniFile
                      help: the ini file with the list of arguments
                  generate-conf-file:
                      type: str
                      help: generate configuration file (ini) containing default values and exits. This file is than can be used with the from-file argument
