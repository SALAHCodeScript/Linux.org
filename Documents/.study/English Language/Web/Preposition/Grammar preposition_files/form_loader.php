
//
// LibWizard Embed bootstrap file
//


function lwz2_embed_initialize() {
    const id = "83c709f6c03d75da9a438f6f07bf00d2";
    const tag = 'form_'+id;
    const iframe_tag = id;
    const title = id;
    const src = "https://waldenu.libwizard.com/id/83c709f6c03d75da9a438f6f07bf00d2";
    const html = '<iframe id="'+iframe_tag+'" name="'+iframe_tag+'" scrolling="auto" title="'+title+'" src="'+src+'" referrerpolicy="no-referrer-when-downgrade" style="width:100%; height:200px; border:0;" allowfullscreen><a href="'+src+'">Go to LibWizard Form</a></iframe>';
    document.getElementById(tag).innerHTML = html;
    initPostMessageListener(id);
}

lwz2_embed_initialize();


function lwz2_embed_autoResize(el) {
    el.contentWindow.postMessage({cmd:"get_size",id:el.id}, "*");
}

function initPostMessageListener(hash) {
try {
    // Here "addEventListener" is for standards-compliant web browsers and "attachEvent" is for IE Browsers.
    const eventMethod = window.addEventListener ? "addEventListener" : "attachEvent";
    const eventer = window[eventMethod];
    const messageEvent = eventMethod == "attachEvent" ? "onmessage" : "message";

    // Listen to message from child (iframe)
    eventer(messageEvent, function (e) {
        const obj = e.data;

        switch(obj.cmd) {
        case "set_size":
            if (obj.id === hash) {
                lwz2_embed_resizeIFrame(obj);
            }
            break;
        case "set_title":
            if (obj.id === hash) {
                lwz2_embed_setTitle(obj);
            }
            break;
        case "form_loaded":
            if (obj.id === hash) {
                const iframe = document.getElementById(obj.id);
                if (!iframe) { return; }
                lwz2_embed_autoResize(iframe);
            }
        break;
        case "scroll_top":
            if (obj.id === hash) {
                const iframe = document.getElementById(obj.id);
                if (!iframe) { return; }
                iframe.scrollIntoView({block: "start", inline: "nearest", behavior: "smooth"});
            }
            break;
        }

    }, false);
}
catch(e) {}
}

function lwz2_embed_resizeIFrame(data) {
  const iframe = document.getElementById(data.id);
  if (!iframe) { return; }
  const form_height = data.height + "px";
  iframe.style.height = form_height;
}

function lwz2_embed_setTitle(data) {
  const iframe = document.getElementById(data.id);
  if (!iframe) { return; }
  iframe.title = data.title;
}
