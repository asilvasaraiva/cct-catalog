## [1.2.0](https://github.com/asilvasaraiva/cct-catalog/compare/v1.1.2...v1.2.0) (2026-08-03)





# [1.2.0](https://github.com/asilvasaraiva/cct-catalog/compare/v1.1.2...v1.2.0) (2026-08-03)


### Features

* added Swagger/OpenAPI docs via drf-spectacular to generate an OpenAPI 3 schema and serve interactive docs at /api/schema/, /api/docs/ (Swagger UI) and /api/redoc/ (Redoc). ([b90ee71](https://github.com/asilvasaraiva/cct-catalog/commit/b90ee71fe18c3da38e6f075774e1e5bf7b8a139c))

## [1.1.2](https://github.com/asilvasaraiva/cct-catalog/compare/v1.1.1...v1.1.2) (2026-08-03)





## [1.1.2](https://github.com/asilvasaraiva/cct-catalog/compare/v1.1.1...v1.1.2) (2026-08-03)


### Bug Fixes

* added  ALLOWED_HOSTS configurable to unblock health probes for argocd readiness access ([9c75be4](https://github.com/asilvasaraiva/cct-catalog/commit/9c75be49129e6c5b14163f39d96bfcdb6b52419a))

## [1.1.1](https://github.com/asilvasaraiva/cct-catalog/compare/v1.1.0...v1.1.1) (2026-08-03)





## [1.1.1](https://github.com/asilvasaraiva/cct-catalog/compare/v1.1.0...v1.1.1) (2026-08-03)


### Bug Fixes

* rising the initial delay  seconds for liveness and readiness argocd ([8cb27db](https://github.com/asilvasaraiva/cct-catalog/commit/8cb27dbbdd19c0d4d31b05d4dd246a396b091acd))

## [1.1.0](https://github.com/asilvasaraiva/cct-catalog/compare/v1.0.0...v1.1.0) (2026-08-03)





# [1.1.0](https://github.com/asilvasaraiva/cct-catalog/compare/v1.0.0...v1.1.0) (2026-08-03)


### Features

* added liveness/readiness health endpoints and wire them into Helm probes ([df2465f](https://github.com/asilvasaraiva/cct-catalog/commit/df2465fc9989b22c0aaf57b37390320bef124e62))

## 1.0.0 (2026-08-02)





# 1.0.0 (2026-08-02)


### Bug Fixes

* Job to build/push docker image ([6afcff0](https://github.com/asilvasaraiva/cct-catalog/commit/6afcff0e9f394deb9dd2a588757a3d36976ac84e))
* test ([9afa229](https://github.com/asilvasaraiva/cct-catalog/commit/9afa22974f2998f84a128d882920b005b99352fa))


### Features

* added docker containerization configuration files, and created docker compose with postgress ([c28552b](https://github.com/asilvasaraiva/cct-catalog/commit/c28552be5e7382b52788868c8184e7fb9edf9ab6))
* Added semantic release and gate image publishing on new releases ([05bdaa9](https://github.com/asilvasaraiva/cct-catalog/commit/05bdaa9775053cb6121dabb9c0cd611f919b9e50))
* adjustment in settings.py and added environment driven database configuration ([979470e](https://github.com/asilvasaraiva/cct-catalog/commit/979470e0aa6b9ede4271458e02a8c732a61f7b89))
* **helm:** add books-catalog-chart Helm chart with Deployment, Service, Ingress, ConfigMap and migration Job ([ace5208](https://github.com/asilvasaraiva/cct-catalog/commit/ace520833148b990847fd00801a4e3b8c66d88fb))
