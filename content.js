console.log("chrome extension ready!!!");


var textContent;

var old=0, latest=0;
var result

var num=1;
var ans = "no hate"
var commWrite =""
var oldText = ""
var commYt = ""
var oldYt = ""
 chrome.runtime.onMessage.addListener(
    function(request, sender, sendResponse) {
      sendResponse({msg: "got it!!!"});
    if(request.url.substring(0,23)=="https://www.youtube.com")
    {        
        setInterval(function(){
              var comments = document.getElementsByTagName("ytd-comment-renderer")

              latest = comments.length
              if(latest>old)
              {
                for(var i=old;i<latest;i++)
                {
                    var inner = comments[i].getElementsByClassName("style-scope ytd-comment-renderer")[22]
                    textContent = inner.innerText
                    // console.log(textContent)
                    var ans = sendText(textContent)
                    console.log(ans)
                    if(ans==="hate and abusive")
                    {
                       inner.innerText = "Ce commentaire a été bloqué  !!!"
                       inner.style ="color:#CE0D00; font-weight:bold";
                       console.log("BLOCKED", textContent);
                       chrome.action.setPopup({ popup: "popup.html" });
                    }
                    else{
                      console.log("unblocked comments: ",textContent)
                    }
                }
                old = Math.max(old,latest)
              }
        },1000)

        setInterval(function(){
          var youtComm = document.getElementById("contenteditable-root")
          commYt = youtComm.innerText
          if(commYt!="" || commYt!=oldYt)
          {
            var commentWritten = sendText(commYt)
            console.log(commentWritten)
            oldYt = commYt
          }
        },8000)
  
      }

function sendText(textContent){
    // result = "BROKEN";
    chrome.runtime.sendMessage({textMsg: textContent}, function(response) {
        result = response.farewell;
        console.log(result)
      });
      return result
}

})