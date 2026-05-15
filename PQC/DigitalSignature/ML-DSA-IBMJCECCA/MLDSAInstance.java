import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.Signature;

import com.ibm.crypto.hdwrCCA.provider.MLDSAKeyParameterSpec;
import com.ibm.crypto.hdwrCCA.provider.MLDSAPrivateKey;
import com.ibm.crypto.hdwrCCA.provider.MLDSAPublicKey;

public class MLDSAInstance {

    public static void main(String[] args) throws Exception {
        // s#1: Creare key pair
	KeyPairGenerator kpg = KeyPairGenerator.getInstance("ML-DSA", "IBMJCECCA");
	MLDSAKeyParameterSpec kps = new MLDSAKeyParameterSpec("puremldsa65");
	
	kpg.initialize(kps, null);
	KeyPair keyPair = kpg.generateKeyPair();

	// s#2: get public and private keys
	MLDSAPrivateKey privKey = (MLDSAPrivateKey) keyPair.getPrivate();
	MLDSAPublicKey pubKey = (MLDSAPublicKey) keyPair.getPublic();
	
	// s#3: create Signature object
	Signature sign = Signature.getInstance("ML-DSA", "IBMJCECCA");
	
	// s#4: initialize Signature for signing
	sign.initSign(privKey);
	
	// s#5: add bytes to Signature
	byte[] data = "Spectre - Let's create".getBytes();
	sign.update(data);
	
	// s#6: perform Signature
	byte[] sigData = sign.sign();
	
	// s#7: initialize the Signature for verification
	sign.initVerify(pubKey);
	sign.update(data);

	// s#8: Verify
	boolean verified = sign.verify(sigData);
	if (verified) {
	    System.out.println("Signature verified");
	} else {
	    System.out.println("Signature could NOT be verified");
	}
    }
}

// Note: "IBMJCECCA" comes bundled with the IBM Java distribution called: IBM Semeru Runtime Certified Edition. Most likely this package doesn't available on macOS because IBM does not ship IBMJCECCA there.
