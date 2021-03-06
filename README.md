# MTG Comrade Deck Legality Checker

This little python script is meant to check Magic: The Gathering decklists' legality for the Comrade custom format.

To use, simply paste your MTGA-format decklist (from moxfield.com or whereever) in the "DECKLIST_TO_CHECK.txt" file, and then open "comrade_legality_checker.exe".

The first time you do this, it will fetch a card database from the scryfall.com API, which takes about 2-3 minutes.
Once you have the database, everything else happens locally: it checks Card names and amounts in your deck as well as some other things and tells you if
the given deck is legal to play in MTG Comrade. Hope this saves a bit of time double-checking decks.

## Download

Simply head to the GitHub pages's ["releases" section](https://github.com/Quatrixx/comrade_legal_checker/releases).

## Author
**Alexander Kitzig** - *"Quatrix"*

&nbsp; 

--- 

This project uses [mtgtools](https://github.com/EskoSalaka/mtgtools) by Esko-Kalervo Salaka, so I include his License and Acknowledgements below:

## License (mtgtools)

Copyright © 2018 Esko-Kalervo Salaka.
All rights reserved.

Zope Public License (ZPL) Version 2.1

A copyright notice accompanies this license document that identifies the
copyright holders.

This license has been certified as open source. It has also been designated as
GPL compatible by the Free Software Foundation (FSF).

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions in source code must retain the accompanying copyright
   notice, this list of conditions, and the following disclaimer.

2. Redistributions in binary form must reproduce the accompanying copyright
   notice, this list of conditions, and the following disclaimer in the
   documentation and/or other materials provided with the distribution.

3. Names of the copyright holders must not be used to endorse or promote
   products derived from this software without prior written permission from the
   copyright holders.

4. The right to distribute this software or to use it for any purpose does not
   give you the right to use Servicemarks (sm) or Trademarks (tm) of the
   copyright
   holders. Use of them is covered by separate agreement with the copyright
   holders.

5. If any files are modified, you must cause the modified files to carry
   prominent notices stating that you changed the files and the date of any
   change.

Disclaimer

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS ''AS IS'' AND ANY EXPRESSED
OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO
EVENT SHALL THE COPYRIGHT HOLDERS BE LIABLE FOR ANY DIRECT, INDIRECT,
INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

## Acknowledgments (mtgtools)

This software uses ZODB, a native object database for Python, which is a
copyright © by Zope Foundation and Contributors.

This software uses Scryfall's rest-like API which is a copyright © by Scryfall LLC.

This software uses rest-like API of magicthegathering.io which is a copyright © by Andrew Backes.

This software uses the Python Imaging Library (PIL) which is a copyright © 1997-2011 by Secret Labs AB and
copyright © 1995-2011 by Fredrik Lundh

All the graphical and literal information and data related to Magic: The Gathering which can be handled with this
software, such as card information and card images, is copyright © of Wizards of the Coast LLC, a
Hasbro inc. subsidiary.

This software is in no way endorsed or promoted by Scryfall, Zope Foundation, magicthegathering.io or
Wizards of the Coast.

This software is free and is created for the purpose of creating new Magic: The Gathering content and software, and
just for fun.
