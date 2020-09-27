# CircleTest
test for CI/CD on CircleCI

# Setup
- Install Docker
- [Install CircleCI CLI](https://circleci.com/docs/ja/2.0/local-cli/#%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB)
    ```bash
    curl -fLSs https://circle.ci/cli | bash
    ```

- Prepare `.circleci/config.yml` (version 2.1)

# Local
- Convert for running on local (required `version 2`, not 2.1)

    ```bash
    circleci config process .circleci/config.yml > .circleci/config_local.yml
    ```

- Run
    ```bash
    circleci local execute -c .circleci/config_local.yml
    ```


# References
https://qiita.com/nemotoy/items/7a9b8958a051df1de40f