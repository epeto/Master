public class MiClaseUtilTest {
    public static void main(String[] args){
        byte[] arrByte = {10, 50, 67, 98, 127, 100, 5, 4, 1, 69, 40};
        short[] arrShort = {10, 50, 67, 98, 200, 100, 5, 4, 1, 69, 40};
        int[] arrInt = {10, 50, 67, 98, 200, 100, 5, 4, 1, 69, 40};
        long[] arrLong = {10, 50, 67, 98, 200, 100, 5, 4, 1, 69, 40};
        float[] arrFloat = {10.1f, 50.2f, 67.3f, 98.4f, 200.5f, 100.6f, 5.7f, 4.8f, 1.9f, 69.10f, 40.11f};
        double[] arrDouble = {10.1f, 50.2, 67.3, 98.4, 200.5, 100.6, 5.7, 4.8, 1.9, 69.10, 40.11};

        System.out.println("Max byte: "+MiClaseUtil.maxInArray(arrByte));
        System.out.println("Max short: "+MiClaseUtil.maxInArray(arrShort));
        System.out.println("Max int: "+MiClaseUtil.maxInArray(arrInt));
        System.out.println("Max long: "+MiClaseUtil.maxInArray(arrLong));
        System.out.println("Max float: "+MiClaseUtil.maxInArray(arrFloat));
        System.out.println("Max double: "+MiClaseUtil.maxInArray(arrDouble));
    }
}
