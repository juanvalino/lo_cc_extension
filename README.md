# CC Extension: LibreOffice calc CryptoCompare market functions

The CC extension allows you to create customized spreadsheets with CryptoCompare market data directly from the web.

## Download   

You can download the current version of the CC Extension from [here](https://github.com/juanvalino/lo_cc_extension/releases).

## Usage

The CC Extension adds these new functions to LibreOffice Calc:
```
GETCCHHISTORICALPRICE(fsym, tsym, exchange, date)

  fsym (string): symbol from wich get the price (from symbol)
  tsym (string): symbol in which the price must be get (to symbol)
  exchange (string): exchange to get the price from (can be an empty '' string if you don't want to use a concrete exchange).   
  date (float): date in LibreOffice calc (days since 1899/12/31)

  Example:
    GETCCHHISTORICALPRICE("BTC", "USD", "Coinbase", 42844.04)
```  

The parameters `fsym`, `tsym` and `exchange` are names supported by the cryptocompare python library.

## Performance

This extension introduces caching of the historical prices returned by `GETCCHHISTORICALPRICE` function. This local cache is stored on `~/.cc_cache.csv`.

## Upgrading

The LibreOffice extension mechanism is poorly documented and extremely fragile. It is **STRONGLY** recommended that you remove the previous version of CC-Extension before adding this one. If you use the replace option you might or might not end up with indecipherable error messages or an unusable extension.

LibreOffice does not handle extension files with spaces in the names well. The spaces usually end up being there because your browser renames files to things like "CC (1).oxt" if there is already a (previous) version in your download directory. If you attempt to install/upgrade using such a file the process will fail and leave the extension in an inconsistent state: it won't appear in the installed extensions list but if you try to install the same version again it will say it is already installed. Take care to remove previous downloads before downloading the latest extension, or to rename it after downloading and remove any spaces from the filename. See bug [114708](https://bugs.documentfoundation.org/show_bug.cgi?id=114708).

If you/LibreOffice really screw things up I recommend closing LibreOffice, renaming the entire customisation directory (~/.config/libreoffice/4 on linux), restarting it and re-installing (all) your extensions.

Recovering from a messed-up extension installation/upgrade is much harder for Windows users. Really, make a system snapshot before installing or upgrading any LibreOffice extension.

## Dependencies

To use this extension you need the [cryptocompare python library](https://pypi.org/project/cryptocompare/) in your system.

## Support

If you find a bug or wish to request a feature please file an issue at the [issue tracker](http://github.com/juanvalino/lo_cc_extension/issues).

## Contribute

Help is always welcome with development.  If you would like to contribute you will need to fork the main repo, make your changes, and send a [pull request](http://github.com/juanvalino/lo_cc_extension/pulls) to have your changes moderated and merged back into the main repo. Details on that process can be found [here](https://help.github.com/articles/set-up-git/).  

## License

The CC Extension is released under the [![][shield:LGPL3]][License:3.0]

## Warranty

There is **NO** warranty of any kind. You use the software entirely at your own risk. I am not responsible if anything goes wrong.

## Author Information

- Juan Antonio Valiño García.
- Based on [Mark Brooker LOC-Extension](https://github.com/walkjivefly/LOC-Extension).

[GIT:release]: http://github.com/juanvalino/lo_cc_extension/releases/latest
[License:3.0]: http://www.gnu.org/licenses/lgpl.html
[shield:LGPL3]: http://img.shields.io/badge/license-LGPL%20v.3-blue.svg
