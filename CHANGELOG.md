# CHANGELOG


## v0.6.2 (2025-07-15)

### Bug Fixes

- Update sok-ble dependency to fix reconnect loop
  ([`6981789`](https://github.com/IAmTheMitchell/sok-ha/commit/698178944024b22398c73eb4ab0ec2c2af90b9c8))

### Chores

- Update AI directives
  ([`932a47a`](https://github.com/IAmTheMitchell/sok-ha/commit/932a47af1961e6e58cc89e0ba68f5f4014f47a99))

### Continuous Integration

- Add ruff
  ([`e8f645e`](https://github.com/IAmTheMitchell/sok-ha/commit/e8f645eb7be1afbb4bec05b94bed3f793670a544))

- Enable dependabot
  ([`fa5cb78`](https://github.com/IAmTheMitchell/sok-ha/commit/fa5cb7896f4379727679aa9a365ec769a630ce3e))

### Documentation

- Add hardware, video, and CI links
  ([`8e9d4e9`](https://github.com/IAmTheMitchell/sok-ha/commit/8e9d4e97b9c0795cd76eb950fb03aba885008825))

### Refactoring

- Fix ruff lint errors
  ([`ad617fb`](https://github.com/IAmTheMitchell/sok-ha/commit/ad617fb1eabb6ad8d9c6ef4f4bf1e2c7681aa183))

- Ruff autofixes
  ([`3425f3e`](https://github.com/IAmTheMitchell/sok-ha/commit/3425f3ead186b6bf3f2f29dd879707bca7dbd097))


## v0.6.1 (2025-06-14)

### Bug Fixes

- Update dir name to match domain
  ([`571b571`](https://github.com/IAmTheMitchell/sok-ha/commit/571b5713bf73fea245c14ae1fc988a09b81ecb47))

- Update domain name (will allow for logos and icons to be populated)
  ([`9a74646`](https://github.com/IAmTheMitchell/sok-ha/commit/9a746465c2c159a76f6d14dd2f8ec568423e5b9e))

- Update path to manifest.json version
  ([`6afd77a`](https://github.com/IAmTheMitchell/sok-ha/commit/6afd77a27d7fdc4d157994fbd0abc092468880a7))

- Update tests for new integration domain
  ([`09050d3`](https://github.com/IAmTheMitchell/sok-ha/commit/09050d3afb01c55888d071fb02feb26120421372))

### Documentation

- Add dashboard image to README
  ([`394e4fa`](https://github.com/IAmTheMitchell/sok-ha/commit/394e4faa40c4a76d200ff1bef7ea09417b4b3132))


## v0.6.0 (2025-06-13)

### Features

- Set voltage precision
  ([`ec5ced6`](https://github.com/IAmTheMitchell/sok-ha/commit/ec5ced6e8c7625f32acc9688daa50022d1255d0e))


## v0.5.0 (2025-06-13)

### Documentation

- Add additional information
  ([`91a531c`](https://github.com/IAmTheMitchell/sok-ha/commit/91a531c5c799f5105f67ba4799baf5ba591597bc))

- Add integration readme
  ([`bd72fbd`](https://github.com/IAmTheMitchell/sok-ha/commit/bd72fbddd67c87bad9f3fef29f61ae2e489db27d))

### Features

- Add energy sensors
  ([`7b4989c`](https://github.com/IAmTheMitchell/sok-ha/commit/7b4989ca002f7fbe43043f187ffe338739461061))


## v0.4.2 (2025-06-10)

### Bug Fixes

- Recover from cancelled BLE connections
  ([`1891507`](https://github.com/IAmTheMitchell/sok-ha/commit/1891507b52dce71ee74e3db3498e65b6569f896e))

- Upgrade sok-ble
  ([`3e16730`](https://github.com/IAmTheMitchell/sok-ha/commit/3e167306aa4af685eb08a3cdfb0c445492cae210))

- Upgrade sok-ble to v0.1.4
  ([`abbe78e`](https://github.com/IAmTheMitchell/sok-ha/commit/abbe78e9b811dd6e13ef8abf0f71227cf70eb4cb))


## v0.4.1 (2025-06-09)

### Bug Fixes

- Log exception type and stacktrace on update failure
  ([`d8f99ba`](https://github.com/IAmTheMitchell/sok-ha/commit/d8f99ba685de79e7ea3ed3dce5d756f32e70488c))


## v0.4.0 (2025-06-09)

### Bug Fixes

- Add retry logic for BLE updates
  ([`895e531`](https://github.com/IAmTheMitchell/sok-ha/commit/895e5312d4cd1ca351cd20e87009606b8a6c90c0))

- Handle missing coordinator data
  ([`72195b4`](https://github.com/IAmTheMitchell/sok-ha/commit/72195b4944d1b238e3469596cf6ccdc79513bd89))

### Features

- Improve debug logging
  ([`b956688`](https://github.com/IAmTheMitchell/sok-ha/commit/b9566883d88c3fb913408e1321dcd6a286ed62d6))

- Improve startup reliability
  ([`94b57bd`](https://github.com/IAmTheMitchell/sok-ha/commit/94b57bd1dedfcf309b7877e813c769aa11a43ed0))


## v0.3.0 (2025-06-09)

### Bug Fixes

- Add explicit name for some entities
  ([`945008c`](https://github.com/IAmTheMitchell/sok-ha/commit/945008c68d7fc9e7941792a7949d4358238933b8))

- Add translation keys for all sensors
  ([`b07a2a9`](https://github.com/IAmTheMitchell/sok-ha/commit/b07a2a9595a5fffc7a9d57b1f43e8d64a4690fdc))

- Add translation keys for missing entity names
  ([`fac9605`](https://github.com/IAmTheMitchell/sok-ha/commit/fac96057acc5c1514037a57b43b648ce1f40aaa0))

- Add translation keys for sensors
  ([`b630958`](https://github.com/IAmTheMitchell/sok-ha/commit/b6309580dedd3bf4da6ff81531cfdbd4da986388))

- Assign icons to some entities
  ([`a87b16e`](https://github.com/IAmTheMitchell/sok-ha/commit/a87b16e3f9c4e8d9bf6ea7486baf8a2fad4b54fa))

- Update soc name to battery
  ([`88e5024`](https://github.com/IAmTheMitchell/sok-ha/commit/88e50249bcb50f8fb581afa583e92cca245d3355))

### Features

- Remove device when entry deleted
  ([`e0ebe22`](https://github.com/IAmTheMitchell/sok-ha/commit/e0ebe22a058a4fc467f372546e1defb06e9d9e17))


## v0.2.0 (2025-06-09)

### Features

- Group sensors under device
  ([`9e4c2bf`](https://github.com/IAmTheMitchell/sok-ha/commit/9e4c2bf861689dff808d93eb5a860f0083b31ec5))


## v0.1.0 (2025-06-09)

### Bug Fixes

- Correct version path for release
  ([`eb45d1b`](https://github.com/IAmTheMitchell/sok-ha/commit/eb45d1bf0ad54bd728f31d8b343a7e2cf487fe05))

- Support older ha bluetooth discovery
  ([`376eafb`](https://github.com/IAmTheMitchell/sok-ha/commit/376eafb6a0f313313d31e9a0d968bc55906f96c8))

- Update sok-ble version
  ([`a324a91`](https://github.com/IAmTheMitchell/sok-ha/commit/a324a91c11713ce77f0161894de6922debe17b0d))

- Update sok-ble version in manifest
  ([`409b10b`](https://github.com/IAmTheMitchell/sok-ha/commit/409b10b12c8e6351bd5da64bc9b94ececec697bd))

### Chores

- Add AGENTS.md
  ([`86ff2d2`](https://github.com/IAmTheMitchell/sok-ha/commit/86ff2d256413b3a768ccf58b65edd991421cec52))

### Features

- Add files as basis for development
  ([`f9a818d`](https://github.com/IAmTheMitchell/sok-ha/commit/f9a818d739134e0653c452b5968a436635062e28))

- Initial commit
  ([`f9d9881`](https://github.com/IAmTheMitchell/sok-ha/commit/f9d98814c93ee56fda1f6cbf5149924787251a41))

- Integrate sok ble library
  ([`60b5f5f`](https://github.com/IAmTheMitchell/sok-ha/commit/60b5f5f9330614ba67f48d2b190f2940b890fcf9))

### Testing

- Add test dependencies
  ([`b529cf6`](https://github.com/IAmTheMitchell/sok-ha/commit/b529cf6f046d98978be377d030a726528325c218))
