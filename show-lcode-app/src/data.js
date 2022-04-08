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
}, []);

export default DATA;
