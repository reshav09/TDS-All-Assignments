---

### GitHubEval LLM Evaluation Configuration

```yaml
prompts:
  - |
    Generate a curl command that fetches ONLY the top 13 most-starred repositories from the "openai" organization using the GitHub API.
    Use descending order for sorting by stars.
    The command must include authorization using a placeholder token: $API_KEY.

providers:
  - id: openrouter:openai/gpt-4o-mini
    config:
      max_tokens: 1024
  - id: openrouter:openai/gpt-4.1-nano
    config:
      max_tokens: 1024
  - id: openrouter:google/gemini-2.0-flash-lite-001
    config:
      max_tokens: 1024

tests:
  - name: correct_github_api_endpoint
    vars: {}
    assert:
      type: contains
      value: "https://api.github.com/orgs/"

  - name: limits_to_13_repos
    vars: {}
    assert:
      type: contains
      value: "per_page=13"

  - name: sorts_by_stars
    vars: {}
    assert:
      type: contains
      value: "sort=stars"

  - name: descending_order
    vars: {}
    assert:
      type: contains
      value: "direction=desc"

  - name: uses_authorization_header
    vars: {}
    assert:
      type: contains
      value: "Authorization: Bearer $API_KEY"

  - name: rubric_eval_correctness
    vars: {}
    assert:
      type: llm-rubric
      rubric: |
        Evaluate the correctness of the generated curl command for the following:
        - API endpoint: Does it use the correct GitHub endpoint for listing org repositories?
        - Parameters: Are `per_page=13`, `sort=stars`, and `direction=desc` included?
        - Authorization: Does it include the correct authorization header using $API_KEY?

        Score each of the following from 1 (poor) to 5 (excellent):
        - endpoint_correctness
        - parameter_accuracy
        - auth_usage

      schema:
        type: object
        properties:
          endpoint_correctness:
            type: number
            minimum: 1
            maximum: 5
          parameter_accuracy:
            type: number
            minimum: 1
            maximum: 5
          auth_usage:
            type: number
            minimum: 1
            maximum: 5
        required: [endpoint_correctness, parameter_accuracy, auth_usage]
        additionalProperties: false

commandLineOptions:
  cache: true
```

### Explanation:

* **prompts**:

  * The prompt asks the model to generate a `curl` command to fetch the top 13 most-starred repositories from the `openai` organization on GitHub.
  * The query specifies the need for sorting by stars in descending order, and authorization via a placeholder token (`$API_KEY`).

* **providers**:

  * This section includes the three models for evaluation:

    * `openrouter:openai/gpt-4o-mini` with a token limit of 1024.
    * `openrouter:openai/gpt-4.1-nano` with a token limit of 1024.
    * `openrouter:google/gemini-2.0-flash-lite-001` with a token limit of 1024.

* **tests**:

  * Each test checks a specific requirement for the generated `curl` command:

    * Correct GitHub API endpoint for the repositories of an organization.
    * Correct `per_page=13` query parameter.
    * Correct sorting of repositories by stars in descending order.
    * Proper use of the authorization header (`Authorization: Bearer $API_KEY`).
  * The last test evaluates the correctness of the generated command using an LLM-based rubric.

* **commandLineOptions**:

  * The configuration specifies the use of caching to optimize repeated tests.

Let me know if you need further clarifications or adjustments!

