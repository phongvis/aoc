document.addEventListener('DOMContentLoaded', function() {
    // Data
    let data,
        puzzleLabels = [];

    // Instantiate vis
    const leader = pv.vis.leaderboard()
        .xDim({ value: d => d.rank, label: 'puzzle' })
        .yDim({ value: d => d.ascore, label: 'score' })
        .xLabels(puzzleLabels);

    // Main entry
    (function() {
        loadData('../data/smarty.json').then(fileObject => {
            formatData(fileObject);

            // Run the first time to build the vis
            updateVis();

            // Rebuild vis when the window is resized
            window.onresize = _.throttle(updateVis, 100);
        });
    })();

    /**
     * Updates vis when window changed.
     */
    function updateVis() {
        // Update size of the vis
        leader.width(window.innerWidth)
            .height(window.innerHeight);

        // Update size of the vis container and redraw
        d3.select('.pv-vis-demo')
            .attr('width', window.innerWidth)
            .attr('height', window.innerHeight)
            .datum(data)
            .call(leader);
    }

    function loadData(filename) {
        return new Promise((resolve, reject) => {
            d3.json(filename, (err, obj) => {
                if (err) {
                    reject(Error('failed to load ' + filename));
                } else {
                    resolve(obj);
                }
            });
        });
    }

    function computePoints(time, timeList, numMembers) {
        timeList = timeList.map(t => +t);
        const idx = timeList.indexOf(+time);
        if (idx === -1) console.error('should find a time', time, timeList);

        return { rank: idx + 1, score: numMembers - idx };
    }

    function formatData(fileObject) {
        const members = fileObject.members,
            numMembers = _.size(members),
            activeMembers = _.pickBy(members, m => m.stars),
            numPuzzles = _.max(_.map(activeMembers, m => _.max(_.keys(m.completion_day_level).map(x => +x)))) * 2,
            timeList = new Array(numPuzzles);

        for (let i = 1; i <= numPuzzles / 2; i++) {
            puzzleLabels.push(i + '.' + 1, i + '.' + 2);
        }

        // Compute time list on each day to infer points
        _.each(activeMembers, m => {
            _.each(m.completion_day_level, (d, i) => {
                const idx = (+i - 1) * 2;
                if (!timeList[idx]) timeList[idx] = [];
                if (!timeList[idx + 1]) timeList[idx + 1] = [];
                if (d[1]) timeList[idx].push(new Date(d[1].get_star_ts));
                if (d[2]) timeList[idx + 1].push(new Date(d[2].get_star_ts));
            });
        });

        // Any identical time point in the list
        timeList.forEach(l => {
            for (let i = 0; i < l.length - 1; i++) {
                if (+l[i] === +l[i + 1]) console.error('duplicate', l[i]);
            }
        });

        // Sort
        timeList.forEach(l => {
            l.sort(d3.ascending);
        });

        // Generate data
        data = _.map(activeMembers, (v, k) => {
            const line = { id: k, name: v.name || 'ano' + k};
            line.points = [];
            _.times(numPuzzles, () => {
                line.points.push({ rank: _.size(activeMembers), score: 0 });
            });

            _.each(v.completion_day_level, (d, i) => {
                const idx = (+i - 1) * 2;
                if (d[1]) line.points[idx] = computePoints(new Date(d[1].get_star_ts), timeList[idx], numMembers);
                if (d[2]) line.points[idx + 1] = computePoints(new Date(d[2].get_star_ts), timeList[idx + 1], numMembers);
            });

            line.totalPoints = d3.sum(line.points, p => p.score);

            if (line.totalPoints !== v.local_score) console.error('points not matched', line, v);

            // Accumulate points
            let sum = 0;
            line.points.forEach(p => {
                sum = p.ascore = sum + p.score;
            });

            // Update labels
            for (let i = 0; i < line.points.length; i++) {
                line.points[i].label = puzzleLabels[i];
            }

            return line;
        });

        data = data.sort((a, b) => d3.descending(a.totalPoints, b.totalPoints)).slice(0, 20);

        console.log(data);
    }
});