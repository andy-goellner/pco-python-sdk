from typing import Mapping, Any


def format_params(params: Mapping[str, Any]) -> Mapping[str, str]:
    formatted_params = {**params}
    if formatted_params.get("include"):
        inclusions = params["include"]
        formatted_params["include"] = ",".join(map(str, inclusions))
    return formatted_params
