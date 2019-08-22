# Task №1

### [Bullet points for Monefy app](./task№1/readme.md)

# Task №2

### [Bullet points for GnuCash app](./task№2/readme.md)
### [Bug report](./task№2/readme.md#bug-report)

# How to install

### Install [Java](https://www.java.com), [Android SDK](https://developer.android.com), [Appium](http://appium.io), [NodeJS](https://nodejs.org)
### or install [HomeBrew](https://brew.sh) and run

```bash
cd task№2 && bash post_clone_android_tests.sh
```

### Then update your environment variables

```bash
export ANDROID_HOME=/users/<user name>/library/android/sdk
export JAVA_HOME=/library/java/JavaVirtualMachines/<installed jdk>/contents/home
```

# How to run

### Check installed emulators

```bash
$ANDROID_HOME/emulator/emulator -list-avds
```

### Run emulator
```bash
$ANDROID_HOME/emulator/emulator @<emulator name from the list of installed emulators>
```

### Run Appium
```bash
appium --port 4723 --address 0.0.0.0
```

### Run tests
```bash
cd task№2 && bash run_android_tests.sh
```

# Task №3

### [Test cases for API tests](./task№3/readme.md)

# How to install

### Install [Pyton 3.6 or above](https://www.python.org) and [NodeJS](https://nodejs.org)
### or install [HomeBrew](https://brew.sh) and run

```bash
brew install node &&
brew install python3
```

### then run
```bash
cd task№3 && bash post_clone_api_tests.sh
```

### to install [API-Playground](https://github.com/BestBuy/api-playground.git), update [NPM modules](https://www.npmjs.com) and install [Python Requests framework](https://pypi.org/project/requests)

# How to run

### Run

```bash
cd task№3 && bash run_api_tests.sh
```
