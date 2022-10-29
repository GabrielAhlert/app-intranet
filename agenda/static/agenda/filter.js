const tablefilter = () => {
  const trs = document.querySelectorAll('.table tr:not(.head)')
  const filter = document.querySelector('.txtSearch').value
  const regex = new RegExp(filter, 'i')
  const isFoundInTds = td => regex.test(td.innerHTML)
  const isFound = childrenArr => childrenArr.some(isFoundInTds)
  const setTrStyleDisplay = ({ style, children }) => {
    style.display = isFound([
      ...children // <-- All columns
    ]) ? '' : 'none' 
  }
  
  trs.forEach(setTrStyleDisplay)
}

document.querySelector('.txtSearch').addEventListener('keyup', tablefilter)
document.querySelector('.txtSearch').focus()
console.log('tablefilter loaded')