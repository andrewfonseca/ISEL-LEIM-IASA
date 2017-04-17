public class ConnectionOperator implements Operator {
    private StateLocation origin_state;
    private StateLocation destination_state;
    private float connection_cost;

    public ConnectionOperator(String initial_location, String final_location, float connection_cost) {
        this.origin_state = new StateLocation(initial_location);
        this.destination_state = new StateLocation(final_location);
        this.connection_cost = connection_cost;
    }

    @Override
    public State apply(State state) {
        if (state.equals(this.origin_state)) {
            return this.destination_state;
        }

        return null;
    }

    @Override
    public Float cost(State state, State successor) {
        return this.connection_cost;
    }
}
