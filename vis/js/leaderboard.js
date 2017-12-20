/**
 * A visualization of leader board.
 */
pv.vis.leaderboard = function() {
    /**
     * Visual configs.
     */
    const margin = { top: 10, right: 80, bottom: 20, left: 40 };

    let visWidth = 960, visHeight = 600, // Size of the visualization, including margins
        width, height; // Size of the main content, excluding margins

    /**
     * Accessors.
     */
    let id = d => d.id,
        points = d => d.points,
        xDim, yDim,
        xLabels,
        name = d => d.name,
        title;

    /**
     * Data binding to DOM elements.
     */
    let data,
        dataChanged = true; // True to redo all data-related computations

    /**
     * DOM.
     */
    let visContainer, // Containing the entire visualization
        lineContainer,
        selectedLineContainer,
        xAxisContainer,
        yAxisContainer;

    /**
     * D3.
     */
    const xScale = d3.scalePoint(),
        yScale = d3.scaleLinear(),
        xAxis = d3.axisBottom().scale(xScale),
        yAxis = d3.axisLeft().scale(yScale),
        line = d3.line().x(d => d.x).y(d => d.y),
        colorScale = d3.scaleOrdinal().range(d3.schemeCategory20),
        listeners = d3.dispatch('click');

    /**
     * Main entry of the module.
     */
    function module(selection) {
        selection.each(function(_data) {
            // Initialize
            if (!this.visInitialized) {
                visContainer = d3.select(this).append('g').attr('class', 'pv-leaderboard');
                lineContainer = visContainer.append('g').attr('class', 'lines');
                xAxisContainer = visContainer.append('g').attr('class', 'x-axis');
                yAxisContainer = visContainer.append('g').attr('class', 'y-axis');

                this.visInitialized = true;
            }

            data = _data;
            update();
        });

        dataChanged = false;
    }

    /**
     * Updates the visualization when data or display attributes changes.
     */
    function update() {
        // Canvas update
        width = visWidth - margin.left - margin.right;
        height = visHeight - margin.top - margin.bottom;

        visContainer.attr('transform', 'translate(' + margin.left + ',' + margin.top + ')');
        xAxisContainer.attr('transform', 'translate(0,' + height + ')');

        xScale.range([ 0, width ]);
        yScale.range([ height, 0 ]);

        /**
         * Computation.
         */
        // Updates that depend only on data change
        if (dataChanged) {
            // Domain scale
            xScale.domain(xLabels);
            yScale.domain([ 0, d3.max(data.map(points).map(points => d3.max(points, yDim.value))) ]).nice();
        }

        // Updates that depend on both data and display change
        computeLayout(data);

        /**
         * Draw.
         */
        // Axes
        xAxisContainer.call(xAxis).call(xLabel);
        yAxisContainer.call(yAxis).call(yLabel);

        // Lines
        const lines = lineContainer.selectAll('.line').data(data);
        lines.enter().append('g').attr('class', 'line').call(enterLines)
            .merge(lines).call(updateLines);
        lines.exit().transition().attr('opacity', 0).remove();
    }

    function enterLines(selection) {
        selection.attr('opacity', 0);

        // Line
        selection.append('path')
            // .style('stroke', d => colorScale(name(d)));

        // Name
        selection.append('text')
            .text(name)
            // .style('fill', d => colorScale(name(d)));
    }

    function updateLines(selection) {
        selection.each(function(d, i) {
            const container = d3.select(this);

            // Transition opacity
            container.transition().attr('opacity', 1);

            // Line
            container.select('path').attr('d', line((points(d))));

            // Name
            container.select('text')
                .attr('x', width + 5)
                .attr('y', d.ty);

            // Points
            const items = container.selectAll('.item').data(d.points);
            items.enter().append('g').attr('class', 'item').call(enterItems)
                .merge(items).call(updateItems);
            items.exit().remove();
        });
    }

    /**
     * Called when new items added.
     */
    function enterItems(selection) {
        selection.append('circle')
            .attr('r', 2)
            .append('title')
                .text(title);
    }

    /**
     * Called when items updated.
     */
    function updateItems(selection) {
        selection.each(function(d) {
            const container = d3.select(this);

            container.select('circle')
                .attr('cx', d.x)
                .attr('cy', d.y)
                // .style('fill', colorScale(name(d3.select(this.parentNode).datum())));
                .style('fill', rankScale(d.rank))
                .style('display', d.score ? 'block' : 'none');
        });
    }

    /**
     * Computes the position of each item.
     */
    function computeLayout(data) {
        data.forEach(d => {
            // Lines
            points(d).forEach((p, i) => {
                p.x = xScale(p.label);
                p.y = yScale(yDim.value(p));
            });

            // Name position
            d.ty = _.last(points(d)).y;
        });
    }

    /**
     * x-axis label.
     */
    function xLabel(selection) {
        selection.selectAll('text.x-label').data([ xDim.label ])
            .enter().append('text')
                .attr('class', 'x-label')
                .text(Object);
        selection.select('text.x-label').attr('transform', 'translate(' + width + ', 0)');
    }

    /**
     * y-axis label.
     */
    function yLabel(selection) {
        selection.selectAll('text.y-label').data([ yDim.label ])
            .enter().append('text')
                .attr('class', 'y-label')
                .attr('dy', '.2em')
                .text(Object);
        selection.select('text.y-label').attr('transform', 'rotate(-90)');
    }

    function rankScale(rank) {
        // if (rank === 1) return d3.hsl(0, 1, 0.3);
        // if (rank <= 3) return d3.hsl(0, 1, 0.5);
        // if (rank <= 10) return d3.hsl(0, 1, 0.7);
        // if (rank <= 100) return d3.hsl(0, 1, 0.9);

        if (rank === 1) return d3.hsl(0, 1, 0.3);
        if (rank <= 2) return d3.hsl(0, 1, 0.5);
        if (rank <= 3) return d3.hsl(0, 1, 0.7);

        return d3.rgb(0, 0, 0, 0.1);
    }

    /**
     * Sets/gets the width of the visualization.
     */
    module.width = function(value) {
        if (!arguments.length) return visWidth;
        visWidth = value;
        return this;
    };

    /**
     * Sets/gets the height of the visualization.
     */
    module.height = function(value) {
        if (!arguments.length) return visHeight;
        visHeight = value;
        return this;
    };

    /**
     * Sets/gets the points for each line.
     */
    module.points = function(value) {
        if (!arguments.length) return points;
        points = value;
        return this;
    };

    /**
     * Sets/gets the x dimension.
     */
    module.xDim = function(value) {
        if (!arguments.length) return xDim;
        xDim = value;
        return this;
    };

    /**
     * Sets/gets the y dimension.
     */
    module.yDim = function(value) {
        if (!arguments.length) return yDim;
        yDim = value;
        return this;
    };

    /**
     * Sets/gets the x-labels.
     */
    module.xLabels = function(value) {
        if (!arguments.length) return xLabels;
        xLabels = value;
        return this;
    };

    /**
     * Sets/gets the unique id accessor.
     */
    module.id = function(value) {
        if (!arguments.length) return id;
        id = value;
        return this;
    };

    /**
     * Sets/gets the tooltip of points.
     */
    module.title = function(value) {
        if (!arguments.length) return title;
        title = value;
        return this;
    };

    /**
     * Sets/gets the tooltip of cells.
     */
    module.cellTitle = function(value) {
        if (!arguments.length) return cellTitle;
        cellTitle = value;
        return this;
    };

    /**
     * Sets the flag indicating data input has been changed.
     */
    module.invalidate = function() {
        dataChanged = true;
    };

    /**
     * Binds custom events.
     */
    module.on = function() {
        const value = listeners.on.apply(listeners, arguments);
        return value === listeners ? module : value;
    };

    return module;
};