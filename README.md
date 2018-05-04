## pylibfreenect installation guide

1. Install libfreenect2 following: https://github.com/OpenKinect/libfreenect2/blob/master/README.md#linux

2. Set environment vatiables

	add these lines to the end of "~/.bashrc": 
  
	"export LIBFREENECT2_INSTALL_PREFIX=$HOME/freenect2"
  
	"export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$LIBFREENECT2_INSTALL_PREFIX/lib"

3. Install: "pip install pylibfreenect2"

Installation refer to: 
	http://r9y9.github.io/pylibfreenect2/stable/index.html

Set environment variables and pathes in Ubuntu, refer to: 

	https://help.ubuntu.com/community/EnvironmentVariables
  
	https://unix.stackexchange.com/questions/67781/use-shared-libraries-in-usr-local-lib
