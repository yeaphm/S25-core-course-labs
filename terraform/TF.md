# Terraform in practice

## Best practices

using terraform fmt 
and validation using terraform validate

.gitignore

storing tokens locally and using them as vars

## Docker Infrastructure Using Terraform

`terraform state show`

```bash
PS E:\Documents\Innop\C3\S2\devops\S25-core-course-labs\terraform> terraform state show docker_container.nginx
# docker_container.nginx:
resource "docker_container" "nginx" {
    attach                                      = false
    bridge                                      = null
    command                                     = [
        "nginx",
        "-g",
        "daemon off;",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = null
    cpu_shares                                  = 0
    domainname                                  = null
    entrypoint                                  = [
        "/docker-entrypoint.sh",
    ]
    env                                         = []
    hostname                                    = "98da2c706b95"
    id                                          = "98da2c706b95be14867bc7296e50d09794ccd599944753850373e8c37999f98d"
    image                                       = "sha256:c59e925d63f3aa135bfa9d82cb03fba9ee30edb22ebe6c9d4f43824312ba3d9b"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "AnotherEfimsContainerName"
    network_data                                = [
        {
            gateway                   = "172.17.0.1"
            global_ipv6_address       = null
            global_ipv6_prefix_length = 0
            ip_address                = "172.17.0.2"
            ip_prefix_length          = 16
            ipv6_gateway              = null
            mac_address               = "02:42:ac:11:00:02"
            network_name              = "bridge"
        },
    ]
    network_mode                                = "bridge"
    pid_mode                                    = null
    privileged                                  = false
    publish_all_ports                           = false
    read_only                                   = false
    remove_volumes                              = true
    restart                                     = "no"
    rm                                          = false
    runtime                                     = "runc"
    security_opts                               = []
    shm_size                                    = 64
    start                                       = true
    stdin_open                                  = false
    stop_signal                                 = "SIGQUIT"
    stop_timeout                                = 0
    tty                                         = false
    user                                        = null
    userns_mode                                 = null
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = null

    ports {
        external = 8080
        internal = 80
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

`terraform state list`

```bash
PS E:\Documents\Innop\C3\S2\devops\S25-core-course-labs\terraform> terraform state list
docker_container.nginx
docker_image.nginx
```

Changes applied:

```bash
PS E:\Documents\Innop\C3\S2\devops\S25-core-course-labs\terraform> terraform apply
docker_image.nginx: Refreshing state... [id=sha256:c59e925d63f3aa135bfa9d82cb03fba9ee30edb22ebe6c9d4f43824312ba3d9bnginx]
docker_container.nginx: Refreshing state... [id=3846435eac0e8e9ff88c27351a961a16e13da52a61c625a0293fcf0a69730998]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the
following symbols:
-/+ destroy and then create replacement

Terraform will perform the following actions:

  # docker_container.nginx must be replaced
-/+ resource "docker_container" "nginx" {
      + bridge                                      = (known after apply)
      ~ command                                     = [
          - "nginx",
          - "-g",
          - "daemon off;",
        ] -> (known after apply)
      + container_logs                              = (known after apply)
      - cpu_shares                                  = 0 -> null
      - dns                                         = [] -> null
      - dns_opts                                    = [] -> null
      - dns_search                                  = [] -> null
      ~ entrypoint                                  = [
          - "/docker-entrypoint.sh",
        ] -> (known after apply)
      ~ env                                         = [] -> (known after apply)
      + exit_code                                   = (known after apply)
      - group_add                                   = [] -> null
      ~ hostname                                    = "3846435eac0e" -> (known after apply)
      ~ id                                          = "3846435eac0e8e9ff88c27351a961a16e13da52a61c625a0293fcf0a69730998" -> (known after apply)
      ~ init                                        = false -> (known after apply)
      ~ ipc_mode                                    = "private" -> (known after apply)
      ~ log_driver                                  = "json-file" -> (known after apply)
      - log_opts                                    = {} -> null
      - max_retry_count                             = 0 -> null
      - memory                                      = 0 -> null
      - memory_swap                                 = 0 -> null
        name                                        = "tutorial"
      ~ network_data                                = [
          - {
              - gateway                   = "172.17.0.1"
              - global_ipv6_prefix_length = 0
              - ip_address                = "172.17.0.2"
              - ip_prefix_length          = 16
              - mac_address               = "02:42:ac:11:00:02"
              - network_name              = "bridge"
                # (2 unchanged attributes hidden)
            },
        ] -> (known after apply)
      - network_mode                                = "bridge" -> null # forces replacement
      - privileged                                  = false -> null
      - publish_all_ports                           = false -> null
      ~ runtime                                     = "runc" -> (known after apply)
      ~ security_opts                               = [] -> (known after apply)
      ~ shm_size                                    = 64 -> (known after apply)
      ~ stop_signal                                 = "SIGQUIT" -> (known after apply)
      ~ stop_timeout                                = 0 -> (known after apply)
      - storage_opts                                = {} -> null
      - sysctls                                     = {} -> null
      - tmpfs                                       = {} -> null
        # (20 unchanged attributes hidden)

      ~ healthcheck (known after apply)

      ~ labels (known after apply)

      ~ ports {
          ~ external = 8000 -> 8080 # forces replacement
            # (3 unchanged attributes hidden)
        }
    }

Plan: 1 to add, 0 to change, 1 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_container.nginx: Destroying... [id=3846435eac0e8e9ff88c27351a961a16e13da52a61c625a0293fcf0a69730998]
docker_container.nginx: Destruction complete after 0s
docker_container.nginx: Creating...
docker_container.nginx: Creation complete after 1s [id=712bc613797381e4570dac0e83a9328eb98780850a2c22cf10adda2730cdc6d9]

Apply complete! Resources: 1 added, 0 changed, 1 destroyed.
```

Input var utilization:

```bash
PS E:\Documents\Innop\C3\S2\devops\S25-core-course-labs\terraform> terraform apply -var "container_name=AnotherEfimsContainerName"
docker_image.nginx: Refreshing state... [id=sha256:c59e925d63f3aa135bfa9d82cb03fba9ee30edb22ebe6c9d4f43824312ba3d9bnginx]
docker_container.nginx: Refreshing state... [id=723ac69f90051cdec1d558b03492c3231b72c24f8e95b96eb013b2adb809e46d]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the
following symbols:
-/+ destroy and then create replacement

Terraform will perform the following actions:

  # docker_container.nginx must be replaced
-/+ resource "docker_container" "nginx" {
      + bridge                                      = (known after apply)
      ~ command                                     = [
          - "nginx",
          - "-g",
          - "daemon off;",
        ] -> (known after apply)
      + container_logs                              = (known after apply)
      - cpu_shares                                  = 0 -> null
      - dns                                         = [] -> null
      - dns_opts                                    = [] -> null
      - dns_search                                  = [] -> null
      ~ entrypoint                                  = [
          - "/docker-entrypoint.sh",
        ] -> (known after apply)
      ~ env                                         = [] -> (known after apply)
      + exit_code                                   = (known after apply)
      - group_add                                   = [] -> null
      ~ hostname                                    = "723ac69f9005" -> (known after apply)
      ~ id                                          = "723ac69f90051cdec1d558b03492c3231b72c24f8e95b96eb013b2adb809e46d" -> (known after apply)
      ~ init                                        = false -> (known after apply)
      ~ ipc_mode                                    = "private" -> (known after apply)
      ~ log_driver                                  = "json-file" -> (known after apply)
      - log_opts                                    = {} -> null
      - max_retry_count                             = 0 -> null
      - memory                                      = 0 -> null
      - memory_swap                                 = 0 -> null
      ~ name                                        = "EfimsNginxContainer" -> "AnotherEfimsContainerName" # forces replacement
      ~ network_data                                = [
          - {
              - gateway                   = "172.17.0.1"
              - global_ipv6_prefix_length = 0
              - ip_address                = "172.17.0.2"
              - ip_prefix_length          = 16
              - mac_address               = "02:42:ac:11:00:02"
              - network_name              = "bridge"
                # (2 unchanged attributes hidden)
            },
        ] -> (known after apply)
      - network_mode                                = "bridge" -> null # forces replacement
      - privileged                                  = false -> null
      - publish_all_ports                           = false -> null
      ~ runtime                                     = "runc" -> (known after apply)
      ~ security_opts                               = [] -> (known after apply)
      ~ shm_size                                    = 64 -> (known after apply)
      ~ stop_signal                                 = "SIGQUIT" -> (known after apply)
      ~ stop_timeout                                = 0 -> (known after apply)
      - storage_opts                                = {} -> null
      - sysctls                                     = {} -> null
      - tmpfs                                       = {} -> null
        # (20 unchanged attributes hidden)

      ~ healthcheck (known after apply)

      ~ labels (known after apply)

        # (1 unchanged block hidden)
    }

Plan: 1 to add, 0 to change, 1 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_container.nginx: Destroying... [id=723ac69f90051cdec1d558b03492c3231b72c24f8e95b96eb013b2adb809e46d]
docker_container.nginx: Destruction complete after 0s
docker_container.nginx: Creating...
docker_container.nginx: Creation complete after 1s [id=98da2c706b95be14867bc7296e50d09794ccd599944753850373e8c37999f98d]

Apply complete! Resources: 1 added, 0 changed, 1 destroyed.
```

`terraform output`

```bash
PS E:\Documents\Innop\C3\S2\devops\S25-core-course-labs\terraform> terraform output
container_id = "755946cae6aa15e743284c44e9de39343e9256752a3e3642436639a3b5f98f0d"
image_id = "sha256:c59e925d63f3aa135bfa9d82cb03fba9ee30edb22ebe6c9d4f43824312ba3d9bnginx"
```

## Yandex Using Terraform:



## Terraform for GitHub

I have configured setup and applied it:

### Import Existing Repository

`terraform import github_repository.repo S25-core-course-labs`

```bash
PS E:\Documents\Innop\C3\S2\devops\S25-core-course-labs\terraform\github> terraform import github_repository.repo S25-core-course-labs
github_repository.repo: Importing from ID "S25-core-course-labs"...
github_repository.repo: Import prepared!
  Prepared github_repository for import
github_repository.repo: Refreshing state... [id=S25-core-course-labs]

Import successful!

The resources that were imported are shown above. These resources are now in
your Terraform state and will henceforth be managed by Terraform.
```

### Look at plan changes

`terraform plan`

```bash
PS E:\Documents\Innop\C3\S2\devops\S25-core-course-labs\terraform\github> terraform plan
github_repository.repo: Refreshing state... [id=S25-core-course-labs]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the
following symbols:
  + create
  ~ update in-place

Terraform will perform the following actions:

  # github_branch_default.master will be created
  + resource "github_branch_default" "master" {
      + branch     = "master"
      + id         = (known after apply)
      + repository = "S25-core-course-labs"
    }

  # github_branch_protection.default will be created
  + resource "github_branch_protection" "default" {
      + allows_deletions                = false
      + allows_force_pushes             = false
      + blocks_creations                = false
      + enforce_admins                  = true
      + id                              = (known after apply)
      + pattern                         = "master"
      + repository_id                   = "S25-core-course-labs"
      + require_conversation_resolution = true
      + require_signed_commits          = false
      + required_linear_history         = false

      + required_pull_request_reviews {
          + required_approving_review_count = 0
        }
    }

  # github_repository.repo will be updated in-place
  ~ resource "github_repository" "repo" {
      + description                 = "Efim devops labs"
      - has_downloads               = true -> null
      ~ has_issues                  = false -> true
      - has_projects                = true -> null
        id                          = "S25-core-course-labs"
        name                        = "S25-core-course-labs"
        # (29 unchanged attributes hidden)
    }

Plan: 2 to add, 1 to change, 0 to destroy.
```

### Apply Terraform Changes

`terraform apply`

```bash
PS E:\Documents\Innop\C3\S2\devops\S25-core-course-labs\terraform\github> terraform apply
github_repository.repo: Refreshing state... [id=S25-core-course-labs]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the
following symbols:
  + create
  ~ update in-place

Terraform will perform the following actions:

  # github_branch_default.master will be created
  + resource "github_branch_default" "master" {
      + branch     = "master"
      + id         = (known after apply)
      + repository = "S25-core-course-labs"
    }

  # github_branch_protection.default will be created
  + resource "github_branch_protection" "default" {
      + allows_deletions                = false
      + allows_force_pushes             = false
      + blocks_creations                = false
      + enforce_admins                  = true
      + id                              = (known after apply)
      + pattern                         = "master"
      + repository_id                   = "S25-core-course-labs"
      + require_conversation_resolution = true
      + require_signed_commits          = false
      + required_linear_history         = false

      + required_pull_request_reviews {
          + required_approving_review_count = 0
        }
    }

  # github_repository.repo will be updated in-place
  ~ resource "github_repository" "repo" {
      + description                 = "Efim devops labs"
      - has_downloads               = true -> null
      ~ has_issues                  = false -> true
      - has_projects                = true -> null
        id                          = "S25-core-course-labs"
        name                        = "S25-core-course-labs"
        # (29 unchanged attributes hidden)
    }

Plan: 2 to add, 1 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

github_repository.repo: Modifying... [id=S25-core-course-labs]
github_repository.repo: Modifications complete after 3s [id=S25-core-course-labs]
github_branch_default.master: Creating...
github_branch_default.master: Creation complete after 2s [id=S25-core-course-labs]
github_branch_protection.default: Creating...
github_branch_protection.default: Creation complete after 5s [id=BPR_kwDONvZp7M4DiVeY]

Apply complete! Resources: 2 added, 1 changed, 0 destroyed.
```

## GitHub Teams Using Terraform






