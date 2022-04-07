let print = console.log
function showBounty(id)
{
    console.log(id)
    const x = document.getElementById(id);
    const p = document.getElementById("bounty_"+id)
    p.hidden = !p.hidden
}

//filter will come from bounty-themes checkboxes
function filterBounties()
{
    const bounty_elements = document.querySelectorAll(".bounty-container .bounty-card")
    const checkboxes = document.querySelectorAll(".bounty-themes .checkbox")
    let filter = []
    for(let i = 0; i < checkboxes.length; i++)
    {
        if(checkboxes[i].checked)
        {
            filter.push(checkboxes[i].value)
        }
    }


    if(filter.length > 0)
    {
        for (let i = 0; i < bounty_elements.length; i++) {
            let _theme = bounty_elements[i].getAttribute("bounty-theme")
            if (filter.indexOf(_theme) < 0) {
                bounty_elements[i].hidden = true;
            }
            else{
                bounty_elements[i].hidden = false;
            }
        }
    }
    else
    {
        for (let i = 0; i < bounty_elements.length; i++) {
            let _theme = bounty_elements[i].getAttribute("bounty-theme")
            bounty_elements[i].hidden = false;
        }
    }
}
