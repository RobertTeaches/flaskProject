function showBounty(id)
{
    console.log(id)
    const x = document.getElementById(id);
    const p = document.getElementById("bounty_"+id)
    p.hidden = !p.hidden
}