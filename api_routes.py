from flask import request, jsonify

def initialize_routes(app, db, collection):
    @app.route('/api/relationships/top-groups/', methods=['GET'])
    def top_groups():
        # Get the region_txt parameter from the query string
        region = request.args.get('region_txt')

        if not region:
            return jsonify({"error": "region_txt parameter is required"}), 400

        # MongoDB aggregation pipeline to count occurrences of each group (gname)
        pipeline = [
            {"$match": {"region_txt": region}},  # Filter by region_txt
            {"$group": {
                "_id": "$gname",  # Group by 'gname'
                "count": {"$sum": 1}  # Count occurrences
            }},
            {"$sort": {"count": -1}},  # Sort by count in descending order
            {"$limit": 5}  # Limit to top 5
        ]

        # Execute the aggregation
        results = collection.aggregate(pipeline)

        # Prepare the results to return as JSON
        top_groups = [{"gname": result["_id"], "count": result["count"]} for result in results]

        return jsonify(top_groups)
