//the importing fo environment variables from a VITE library which reads the .env file 
const API_URL = import.meta.env.API_URL

//Param endpoint-->Takes in endpoint
//Param method -->sp
export async function requestAPI(
    //Parameters for this functions contain metadata that would be needed to make an API request
    //the endpoint for the specific router that a request is made to 
    //the method for that router
    //the body/ data that might be needed by that endpoint and router for POST
    //the token needed for authentication
    endpoint,
    method ="GET",
    data = null,
    token = null
) {
    
//Obj to determine the format in which the request is made
const options = {
    method:method,
    //Obj to determine the format in which the request is made,which will be via a JSON string
    headers:{"Content-Type":"application/json"}
};
//Attach data/ a body if a post request is made 
if (data){
    options.body = JSON.stringify(data)
}

//If the API request requires authentication
if (token){
    
    options.headers["Authorization"]=`Bearer ${token}`
}


//Variable that will take in the response from the API
const response = await fetch( `${API_URL}${endpoint}`, options);

//Error handling for unsuccessful requests
if (!response.ok){
    //The error data is assigned the parsed json used to create response obj ,which carries details relating to the API error
    const errorData = await response.json();
    //Print error and error data obj
    console.error("API Error",errorData)

    //Error handling 
    throw new Error(errorData.detail || "API request failed ")

}

//successful requests
//resultant constant is assigned the parsed json used to create response obj
const resultant = response.json()

return resultant
};

export async function apiConnectionCheck() {
    try{
        console.log("Backend connection testing...");
        const api_response = await fetch(API_URL);

        const data = await api_response.json()

        console.log("Successful Connection !")

        console.log("API response",data)

        return true
    }
    catch(error){

        console.error("Backend not connected")

        console.error(error)    
        
        return false
    }
}