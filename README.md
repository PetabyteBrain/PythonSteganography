<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/PetabyteBrain/PythonSteganography">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Python Steganography</h3>

  <p align="center">
    This project is a GUI-based steganography tool that allows users to securely hide and retrieve encrypted messages within images. It supports multiple LSB-based steganography methods and uses RSA encryption to ensure message confidentiality.
    <br />
    <a href="https://github.com/PetabyteBrain/PythonSteganography"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/PetabyteBrain/PythonSteganography">View Demo</a>
    ·
    <a href="https://github.com/PetabyteBrain/PythonSteganography/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/PetabyteBrain/PythonSteganography/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

This Secure Steganography Tool allows users to hide encrypted messages inside images using various LSB (Least Significant Bit) encoding methods. It leverages RSA encryption to ensure only authorized recipients can retrieve the hidden data. The tool provides an intuitive interface to set up a key directory, generate public-private key pairs, and securely encode/decode messages within image files. It is designed for ease of use while maintaining strong security.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python.py]][Python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

The first step to using the tool is to clone the Repo, after that you can install all the needed Prerequisites and run the `run.py` script.

### Prerequisites

Either you can install the Prerequisites manually or there is the possibility of using the Requirements.txt file to automatically install all the needed Libraries
##### 1. Manual install
1. [Pillow](https://pypi.org/project/Pillow/)
    - Shell: `pip install Pillow`
2. [cryptography](https://pypi.org/project/cryptography/)
    - Shell: `pip install cryptography`
  
##### 2. Automatic install
To install all necessary libraries you can just download the requirements.txt file and run this line of code in the command line.
``` bash 
pip install -r requirements.txt
```

<!-- USAGE EXAMPLES -->
## Usage

After running the script, follow these steps to use the Secure Steganography Tool:

1. Set Key Directory – Click the "Set Key Directory" button to choose a folder where your RSA keys will be stored.
2. Generate Keys – Click "Generate Keys" to create a public-private key pair for encryption and decryption.
3. Select Encoding Method – Choose an LSB encoding method:
    - Easy: Least significant bit of red channel.
    - Medium: Two least significant bits of red channel.
    - Hard: Three least significant bits of red channel.
4. Encrypt Message – Enter a message in the text box, select an image, and save the encrypted image.
5. Decrypt Message – Select an encrypted image and retrieve the hidden message using the private key.

This tool ensures secure and easy steganographic encryption and decryption using RSA.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

This Readme file is under the MIT License and the Rest of the Project is under the GNU General Public License. See `LICENSE.txt` for more information.

### MIT License 
```
MIT License

Copyright (c) 2021 Othneil Drew

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Spyros Catéchis - spyroscatechis@proton.me

Project Link: [https://github.com/PetabyteBrain/PythonSteganography](https://github.com/PetabyteBrain/PythonSteganography)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()
* []()
* []()
* [Github Readme Template](https://github.com/othneildrew/Best-README-Template)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/PetabyteBrain/PythonSteganography.svg?style=for-the-badge
[contributors-url]: https://github.com/PetabyteBrain/PythonSteganography/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/PetabyteBrain/PythonSteganography.svg?style=for-the-badge
[forks-url]: https://github.com/PetabyteBrain/PythonSteganography/network/members
[stars-shield]: https://img.shields.io/github/stars/PetabyteBrain/PythonSteganography.svg?style=for-the-badge
[stars-url]: https://github.com/PetabyteBrain/PythonSteganography/stargazers
[issues-shield]: https://img.shields.io/github/issues/PetabyteBrain/PythonSteganography.svg?style=for-the-badge
[issues-url]: https://github.com/PetabyteBrain/PythonSteganography/issues
[license-shield]: https://img.shields.io/github/license/PetabyteBrain/PythonSteganography.svg?style=for-the-badge
[license-url]: https://github.com/PetabyteBrain/PythonSteganography/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/spyros-catechis/
[product-screenshot]: images/screenshot.png
[Python.py]: https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue
[Python-url]: https://python.org/
