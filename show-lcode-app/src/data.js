import DATA from "./lcode-react.json";

// [ { id: 'Two-Sum', count: 3 } ]
export const ALL_TAG_LIST = DATA.reduce((acc, cur) => {
  cur.Tags.forEach((tag) => {
    const targetTagIndex = acc.findIndex((target) => target.id === tag);
    if (targetTagIndex !== -1) {
      acc[targetTagIndex].count += 1;
    } else {
      acc.push({ id: tag, count: 1 });
    }
  });
  return acc;
}, []).sort((a, b) => {
    if (a.id > b.id) return 1;
        else if (a.id === b.id) return 0;
        else return -1;
});

// [ { id: 1, name: 'Easy', count: 12} ]
let levelListInit = [
  {
    id: 1,
    name: "Easy",
    count: 0,
  },
  {
    id: 2,
    name: "Medium",
    count: 0,
  },
  {
    id: 3,
    name: "Hard",
    count: 0,
  },
];
export const ALL_LEVEL_LIST = DATA.reduce((acc, cur) => {
  const targetIdx = acc.findIndex((target) => target.id === cur.Level);
  acc[targetIdx].count += 1;
  return acc;
}, levelListInit);

export default DATA;
