const itemsAdvantage = [
    "Blew Foreward:\n---\nYou have been blown foreward, move up two steps. Tell the group your favorite country",
    "Teleport:\n---\nMove up to the nearest player in front of you. If you are the first player move up 3 steps",
    "Nitrous:\n---\nYou received a sudden boost of gas, move up 2 steps",
    "Pushed foreward:\n---\nAnother person escaping the Taifun rammed you, giving a speed boost, move up 1 step",
    "Muffler Malfunction:\n---\nThe muffler is blasting air giving you a push forward, go up one step",
    "ERS:\n---\nYou receive a sudden boost of energy. Tell the group your favorite car brand, then move up one step",
    "DRS:\n---\nYou recieved a two boost energy pack. Keep this in mind as you can use this anytime you want!",
    "Balloon Vendor:\n---\nYou saw a balloon vendor with a panda balloon. You buy it and attach it to your roof. You suddenly take flight, move up two steps",
    "Out of Creativity:\n---\nThe dev ran out of ideas, move up one step",
    "treeeeeeeeee:\n---\nA tree crashed behind you giving you a boost, move up one step",
    "Robin Hood:\n---\nYou were given a friendly push by a random guy, move up one step"
];

const itemsDisadvantage = [
    "Blew back:\n---\nYou have been blown back, move back two steps",
    "Teleport²:\n---\nMove back to the nearest player behind of you. If you are the last player move back 3 steps",
    "Nitrous²:\n---\nYou received a sudden boost of gas, unfortunately, it came out the front, must be a malfunction. Go back one step",
    "Rammed off:\n---\nAnother person escaping the Taifun pulled a 'George Russel' and rammed you off the mountain, move down a row",
    "Bumper down:\n---\nThe bumper broke, forcing you to fix it. Since you lost time, move back two steps",
    "ICE CREAM!!!:\n---\nYou saw an irregular ice cream vendor who has your favorite ice cream. Tell the group your favorite ice cream flavor, then move back one steps for the time you lost",
    "Friendly Neighbor:\n---\nYou saw your neighbor with his engine broken down. You stop to help them. Move back one step for the time you lost",
    "Balloon Vendor²:\n---\nYou saw a(nother) balloon vendor. You attach the balloon to your roof, unfortunately, you took flight backwards, move back 2 steps",
    "Smushed like an ant:\n---\nYour car got smashed by a tree. Looks like you got to make the journey by feet. Move half the amount you roll, and if it is a one you dont move! If its an odd number, round the decimal down",
    "Out of Creativity²:\n---\nThe dev ran out of ideas, go back a step",
    "Masked Bandit:\n---\nYou were robbed of your nitrous by the masked bandit. Nitrous doesn't work on you anymore"
];

const show = (c, t) => {
    let d = document.getElementById('cardDisplay');
    d.innerHTML = `<p>${c[~~(Math.random()*c.length)]}</p>`;
    d.className = `card-display ${t}-card`;
};

document.getElementById('advantageBtn').onclick = () => show(itemsAdvantage, 'advantage');
document.getElementById('disadvantageBtn').onclick = () => show(itemsDisadvantage, 'disadvantage');
document.getElementById('quitBtn').onclick = () => {
    document.getElementById('cardDisplay').innerHTML = '<p class="prompt">🎉🎉🎉🎉\n\nThank you for using randomiser\nDeveloped by Adi Momin\n\n👋</p>';
    document.querySelectorAll('.card-btn').forEach(b => b.disabled = true);
};
