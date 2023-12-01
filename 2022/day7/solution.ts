export function partOne(data: string[]): number {
  const d: Record<string, number> = { "/": 0 };
  let path = '/';

  data.forEach(row => {
    const line = row.split(" ");

    if (line[0] === "$" && line[1] === "cd" && line[2] !== "/") {
      if (line[2] === "..") {
        const l = path.split("-");
        path = path === "/" ? path : l.slice(0, l.length - 1).join("-");
      } else {
        path = path + '-' + line[2];
      }
    } else {
      const fileSize = Number(line[0]);

      if (!Number.isNaN(fileSize)) {
        d[path] = (d[path] || 0) + fileSize;
        const l = path.split('-');

        for (let i = 0; i < l.length; i++) {
          const p = l.slice(0, i).join('-');
          d[p] = (d[p] || 0) + fileSize;
        }
      }
    }
  });

  return Object.values(d).filter(i => i <= 100000).reduce((acc, i) => acc + i, 0);
}

export function partTwo(data: string[]): number {
  const d: Record<string, number> = { "/": 0 };
  let path = '/';

  data.forEach(row => {
    const line = row.split(" ");

    if (line[0] === "$" && line[1] === "cd" && line[2] !== "/") {
      if (line[2] === "..") {
        const l = path.split("-");
        path = path === "/" ? path : l.slice(0, l.length - 1).join("-");
      } else {
        path = path + '-' + line[2];
      }
    } else {
      const fileSize = Number(line[0]);

      if (!Number.isNaN(fileSize)) {
        d[path] = (d[path] || 0) + fileSize;
        const l = path.split('-');

        for (let i = 0; i < l.length; i++) {
          const p = l.slice(0, i).join('-');
          d[p] = (d[p] || 0) + fileSize;
        }
      }
    }
  });

  const diff = 30000000 - (70000000 - d['/']);

  return Object.values(d).filter(i => i >= diff).sort((a, b) => a - b)[0];
}
