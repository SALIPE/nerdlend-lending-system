export const URI = "http://192.168.90.106";

function internalGet(url, headers) {
  const requestOptions = {
    method: "GET",
    headers,
  };
  return fetch(getUrl(url), requestOptions);
}

function internalPost(url, body, isJson, headers) {
  var requestOptions = {
    method: "POST",
    headers: headers,
  };
  if (body) {
    requestOptions.body = isJson ? JSON.stringify(body) : body;
  }
  return fetch(getUrl(url), requestOptions);
}

function internalDelete(url, headers) {
  var requestOptions = {
    method: "DELETE",
    headers: headers,
  };
  return fetch(getUrl(url), requestOptions);
}

function internalPut(url, body, isJson, headers) {
  var requestOptions = {
    method: "PUT",
    headers: headers,
  };
  if (body) {
    requestOptions.body = isJson ? JSON.stringify(body) : body;
  }
  return fetch(getUrl(url), requestOptions);
}

function internalPatch(url, body, isJson, headers) {
  var requestOptions = {
    method: "PATCH",
    headers: headers,
  };
  if (body) {
    requestOptions.body = isJson ? JSON.stringify(body) : body;
  }
  return fetch(getUrl(url), requestOptions);
}

export async function get(url) {
  return internalGet(url, getHeaders(url)).then(handleJsonResponse);
}



export async function post(url, body) {
  return internalPost(url, body, true, getHeaders(url)).then(
    handleJsonResponse
  );
}

export async function del(url) {
  return internalDelete(url, getHeaders(url)).then(handleJsonResponse);
}

export async function put(url, body) {
  return internalPut(url, body, true, getHeaders(url)).then(handleJsonResponse);
}

export async function patch(url, body) {
  return internalPatch(url, body, true, getHeaders(url)).then(handleJsonResponse);
}

export async function postNoResponse(url, body) {
  return internalPost(url, body, true, getHeaders(url)).then(
    async (response) => {
      isAuthenticate(response);
      if (!response.ok) {
        const { error } = await response.json();
        console.error(error);
        throw Error(error.name);
      }
      return response;
    }
  );
}

async function handleJsonResponse(response) {
  isAuthenticate(response);
  if (!response.ok) {
    const error = await response.json();
    console.error(error);
    throw Error(error.message);
  }
  return await response.json();
}

function getUrl(url) {
  if (url.includes("http")) {
    return url;
  } else {
    return URI + url;
  }
}

export function getHeaders(url) {
  return {
    "Content-Type": "application/json",
    Authorization: `Bearer ${sessionStorage.getItem("user")}`,
  };
}

function isAuthenticate(response) {
  if (response.status === 401 || response.status === 403) {
    cleanStorage();
    window.location.assign("/");
  }
}

export async function logoutSystem() {
  // const requestOptions = {
  //     method: 'POST',
  //     headers: {
  //         'Content-Type': 'application/json',
  //         'Authorization': sessionStorage.getItem('user'),
  //         'Access-Control-Allow-Origin': '*',
  //         'Context': sessionStorage.getItem('context')
  //     },
  // };
  // await fetch(URI + '/users/logout', requestOptions)
  cleanStorage();
  window.location.assign("/");
}

export function cleanStorage() {
  sessionStorage.removeItem("user");
  sessionStorage.removeItem("context");
  sessionStorage.removeItem("company");
  sessionStorage.removeItem("userMenus");
  sessionStorage.removeItem("contextName");
  sessionStorage.removeItem("authorized");
  sessionStorage.removeItem("tribute");
  sessionStorage.removeItem("personDocument");
}

export function getContext() {
  let url = window.location.href;
  let initIdx = url.indexOf("//") + 2;
  let lastIdx = url.indexOf(".");
  if (lastIdx < 0) {
    lastIdx = url.lastIndexOf(":");
  }
  url = url.substring(initIdx, lastIdx);
  return url;
}
