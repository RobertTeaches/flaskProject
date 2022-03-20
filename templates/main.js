function showBounty(id)
{
    console.log(id)
    const x = document.getElementById(id);
    const p = document.getElementById(id + "_bounty")
    p.hidden = !p.hidden
}