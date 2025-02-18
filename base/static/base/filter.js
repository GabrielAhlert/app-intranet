const tablefilter = () => {
	const trs = document.querySelectorAll('.table tr:not(.head)');
	const filter = document.querySelector('.txtSearch').value.trim().toLowerCase();

	if (!filter) {
		trs.forEach(tr => tr.style.display = '');
		return;
	}

	const filterWords = filter.split(/\s+/);

	const isFoundInTds = td => {
		const text = td.textContent.toLowerCase();
		return filterWords.every(word => text.includes(word));
	};

	const isFound = childrenArr => childrenArr.some(isFoundInTds);

	trs.forEach(tr => {
		tr.style.display = isFound([...tr.children]) ? '' : 'none';
	});
};

document.querySelector('.txtSearch').addEventListener('keyup', tablefilter);
document.querySelector('.txtSearch').focus();
