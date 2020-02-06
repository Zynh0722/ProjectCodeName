# \<ProjectCodeName> User Manual

## For now we can just use this to record all the links we're using

### Laptop convert to Linux
* https://www.ifixit.com/Guide/How+to+convert+a+generic+Chromebook+to+Linux+OS/108259

### Set up repo on dev laptops
* Create a [virtual environment](https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html)
  * Open pycharm
  * `ctrl + alt + s` to open settings
  * search for `interpreter`
  * Click on the settings gear next to the `project interpreter`
  * Click on `add`
  * If the `base interpreter` field is blank:
    * Click on the `...` next to `base interpreter`
    * Navigate to `C:\Program Files (x86)\Python36-32\python.exe` and select that
    * Click `okay`
  * Click `okay`
  * Click `apply`
  * Click `OK`
* Install requirements
  * open requirements.txt
  * click `install requirements`
* Install modules
  * open the terminal in pycharm
  * enter `pip install -e .`

### toga examples
* https://github.com/beeware/toga/tree/master/examples