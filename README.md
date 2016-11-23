# dsc-datatool---Spec-and-RPM

This is a SPEC file for CentOS 7.2 for building the dsc-datatool xml transcoder for DSC collected data.
The RPM could be build be running "rpmbuild -ba dsc-datatool.spec" in a CentOS 7.2 build environment.

At the moment the github is containing the necessary RPMs for the dependencies of the prebuilded dsc-datatool RPM.
A move to DSC OARC repo is expected ( https://github.com/DNS-OARC/dsc-datatool )

To install:

- install newest epel-release RPM ( this github repo contains epel release RPM 7-8, but it won't be maintained here !!! )
- install the included perl-RPMS
- install dsc-datatool RPM
- be happy and use


