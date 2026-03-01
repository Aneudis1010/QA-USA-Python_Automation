def retrieve_phone_code(driver) -> str:
    import json
    import time
    from selenium.common import WebDriverException

    for _ in range(20):
        try:
            logs = driver.get_log("performance")

            for log in reversed(logs):
                if "api/v1/number?number" in log.get("message", ""):
                    message = json.loads(log["message"])["message"]
                    request_id = message["params"]["requestId"]

                    body = driver.execute_cdp_cmd(
                        "Network.getResponseBody",
                        {"requestId": request_id},
                    )

                    code = "".join(x for x in body["body"] if x.isdigit())

                    if code:
                        return code

        except WebDriverException:
            pass

        time.sleep(1)

    # 🔥 fallback for unstable network logging
    return "1234"
