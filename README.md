# Compendium Project
This repository is part of the Compendium Project that built a proof of concept for leveraging the biometric security capabilities found on mobile devices for desktop/laptop security. The project developed a number of protocols and applications to provide a general purpose framework for storing and accessing biometrically protected credentials on a mobile device. A security analysis of the protocols has been undertaken using Tamarin.

The project developed both the backend services and an Android demonstrator app. The framework has been integrated with our previously developed virtual authenticator to show the use of biometrics for secure storage of data on the PC and for performing a biometrically protected user verification.

The list of relevant repositories is as follows:
* [Compendium Library](https://github.com/UoS-SCCS/Compendium-Library) - Provides the Python library to be included by the PC based app that wishes to use the protocol
* [Compendium App](https://github.com/UoS-SCCS/Compendium-Android) - The Android app that provides the companion device functionality
* [Compendium PushServer](https://github.com/UoS-SCCS/Compendium-PushServer) - Provides back-end functionality for the communications protocol
* [Virtual Authenticator with Compendium](https://github.com/UoS-SCCS/VirtualAuthenticatorWithCompendium-) - An extension of development Virtual Authenticator which includes Compendium for secure storage of config data and user verification
* [Security Models](https://github.com/UoS-SCCS/Companion-Device---Tamarin-Models-) - Tamarin security models of the protocol

# Security Models
This project holds the tamarin models for the companion device project.
